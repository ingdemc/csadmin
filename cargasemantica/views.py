from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from cargasemantica.models import Metadatos
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import metadatosf
import psycopg2
import psycopg2.extras

# Create your views here.
def index(request):
    return render(request, "index.html")

def calificacion(request):
    return render(request, "calificacion.html" )
     


def crearconexion(request):
     if request.method == 'POST':
         form = metadatosf(request.POST)
         if form.is_valid():
            metadatos = form.save(commit=False)
            metadatos.author = request.user
            metadatos.save()
            return redirect('/verconexion')
     else:
            form = metadatosf()
     return render(request, 'crearconexion.html', {'form': form})

  
def dashboard(request):
    return render(request, "dashboard.html")


def comentarios(request):
    
    metadatos=Metadatos.objects.get(id=id)
    return render(request, 'comentarios.html', {'comentarios_met': metadatos})

def eliminacion(request,id,view):

    metadatos=Metadatos.objects.get(id=id)
    metadatos.delete()

    return redirect('/verconexion')

def recursividad(request,view,id):

    idmet= Metadatos.objects.get(id=id)
    print(idmet)
    # hostdb=str(idmet.nomhost)
    nombd=str(idmet.nombd)
    usuariobd=str(idmet.usuario)
    usuariopass=str(idmet.passw)
    conection2=(" dbname="+nombd+ " user="+usuariobd+" password="+usuariopass)
    con = psycopg2.connect (conection2)
    

    if view == "schema":
        print(con)
        return(schema(con,request,idmet)) 
    else:
        print("algo salio mal en schema")

    if view == "tablas":
        return(tablas(con,request,idmet)) 
    else:
        print("algo salio mal tablas")

    if view == "comentarios":
        return(comentarios(con,request,idmet))
    else: 
        print("algo salio mal comentarios")
        
    if view == "reglas":
        return(reglas(con,request,idmet))
    else: 
        print("algo salio mal reglas")

    
def schema(con,request,idmet):
        
        sql=""" SELECT n.nspname AS "Name",                                          
    pg_catalog.pg_get_userbyid(n.nspowner) AS "Owner",                 
    pg_catalog.array_to_string(n.nspacl, E'\n') AS "Access privileges",
    pg_catalog.obj_description(n.oid, 'pg_namespace') AS "Description" 
    FROM pg_catalog.pg_namespace n                                       
    WHERE n.nspname !~ '^pg_' AND n.nspname <> 'information_schema'      
    ORDER BY 1; """
        try:
                cur = con.cursor()
                cur.execute(sql)
                row=cur.fetchall()   

                for fila in row :
                    for col in fila:
                        print(col, " ", end=" ")
                    print(" ")

                    

                return render(request, 'schema.html', {'schema_met':row, 'metadatos':idmet})

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)
        finally:
            if con is not None:
                        con.close()
                        print('Conexión finalizada.')

    #tablas de las tablas bd
def tablas(con,request,idmet):
    
      sql=""" SELECT table_catalog,table_schema,table_name,table_type FROM information_schema.tables; """
      try:
               cur = con.cursor()
               cur.execute(sql)
               row=cur.fetchall()
              
               
             
               
            #    return data
               return render(request, 'tablasbd.html', {'tablas_met': row,'metadatos':idmet})
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')

def reglas(con,request,idmet):

    
      sql=""" SELECT c.conname                                 AS constraint_name,                                   
     sch.nspname                                   AS "self_schema",
     tbl.relname                                   AS "self_table",
     ARRAY_AGG(col.attname ORDER BY u.attposition) AS "self_columns",
     f_tbl.relname                                 AS "foreign_table",
     ARRAY_AGG(f_col.attname ORDER BY f_u.attposition) AS "foreign_columns",
     pg_get_constraintdef(c.oid)                   AS definition
     FROM pg_constraint c
          LEFT JOIN LATERAL UNNEST(c.conkey) WITH ORDINALITY AS u(attnum, attposition) ON TRUE
          LEFT JOIN LATERAL UNNEST(c.confkey) WITH ORDINALITY AS f_u(attnum, attposition) ON f_u.attposition = u.attposition
          JOIN pg_class tbl ON tbl.oid = c.conrelid
          JOIN pg_namespace sch ON sch.oid = tbl.relnamespace
          LEFT JOIN pg_attribute col ON (col.attrelid = tbl.oid AND col.attnum = u.attnum)
          LEFT JOIN pg_class f_tbl ON f_tbl.oid = c.confrelid
          LEFT JOIN pg_namespace f_sch ON f_sch.oid = f_tbl.relnamespace
          LEFT JOIN pg_attribute f_col ON (f_col.attrelid = f_tbl.oid AND f_col.attnum = f_u.attnum)
     GROUP BY constraint_name, "self_schema", "self_table", definition, "foreign_table"
     ORDER BY "self_schema", "self_table";"""
      try:
               cur = con.cursor()
               cur.execute(sql)
               row=cur.fetchall()
               
             
               
               return render(request, 'reglas.html', {'reglas_met': row,'metadatos': idmet})
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')

def comentarios(con,request,idmet):
     
      sql="""  SELECT c.table_schema,c.table_name,c.column_name,pgd.description
        FROM pg_catalog.pg_statio_all_tables as st
        inner join pg_catalog.pg_description pgd on (pgd.objoid=st.relid)
        inner join information_schema.columns c on (pgd.objsubid=c.ordinal_position
        and  c.table_schema=st.schemaname and c.table_name=st.relname);"""
      try:
               cur = con.cursor()
               cur.execute(sql)
               row=cur.fetchall()
              
        
               return render(request, 'comentarios.html', {'comentarios_met': row,'metadatos': idmet})
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')



class ConexionListView(ListView):
    model=Metadatos 
    template_name= 'tables.html'


    def get_queryset(self):
        # return Curso.objects.filter(creditos__lte=4)
        return Metadatos.objects.all().order_by('id')
    
    def get_context_data(self, **kwargs):
       context =super().get_context_data(**kwargs)
       context['titulo'] = 'Crear_conexion_bd'
       
       return context


