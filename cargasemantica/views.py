from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from cargasemantica.models import Metadatos
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.conf import settings


from .forms import UsersLoginForm,metadatosf,soporte
import psycopg2
import psycopg2.extras




# Create your views here.
def index(request):
    return render(request, "index.html")


# def login(request):
#     return render(request, "login.html")

def register(request):
     return render(request, "register.html")

def calificacion(request):
    return render(request, "calificacion.html" )
     
def soportes(request):
     if request.method == 'POST':
         form = soporte(request.POST)
         if form.is_valid():
            metadatos = form.save(commit=False)
            metadatos.author = request.user
            metadatos.save()
           
            return redirect('/soportes')
     else:
            form = soporte()
     return render(request, 'soporte.html', {'form': form})

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




# def metadatos(request):

#     return render(request, "metadatos.html")

def comentarios(request):
    
    metadatos=Metadatos.objects.get(id=id)
    return render(request, 'comentarios.html', {'comentarios_met': metadatos})

def tablas(request,id):
      
      metadatos=Metadatos.objects.get(id=id)
      print(metadatos)
      con = psycopg2.connect(host="localhost", database="baseuno", user="postgres", password="i076117")
      sql=""" SELECT table_catalog,table_schema,table_name,table_type FROM information_schema.tables; """

      try:
               cur = con.cursor()
               cur.execute(sql)
               row=cur.fetchone()
            #    while row is not None:
            #        print(row)
            #        row=cur.fetchone()
            #    cur.execute(sql)  
               for row in  cur:
                   data= {}
               data = [row[0] for row in cur.fetchall()]
               
             
               
            #    return data
               return render(request, 'tablasbd.html', {'tablas_met': data})
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')

def reglas(request,id):
      
      metadatos=Metadatos.objects.get(id=id)
      print(metadatos)
      con = psycopg2.connect(host="localhost", database="baseuno", user="postgres", password="i076117")
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
               row=cur.fetchone()
            #    while row is not None:
            #        print(row)
            #        row=cur.fetchone()
            #    cur.execute(sql)  
               for row in  cur:
                   print(row)
               data = [row[0] for row in cur.fetchall()]
             
               
            #    return data
               return render(request, 'reglas.html', {'reglas_met': metadatos})
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')


def eliminacion(request,id):

    metadatos=Metadatos.objects.get(id=id)
    metadatos.delete()

    return redirect('/verconexion')


def schema(request,id):
      metadatos=Metadatos.objects.get(id=id)
      print(metadatos)
      con = psycopg2.connect(host="localhost", database="baseuno", user="postgres", password="i076117")
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
               row=cur.fetchone()
               while row is not None:
                   print(row)
                   row=cur.fetchone()
               cur.execute(sql)  
            #    for row in  cur:
            #        print(row)
               data = [row[0] for row in cur.fetchall()]
             
               
            #    return data
               return render(request, 'schema.html', {'schema_met': data})

      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')



# def schema(request,id):
#     metadatos=Metadatos.objects.get(id=id)   
#     print(metadatos)
#     return render(request, 'schema.html', {'schema_met': metadatos})

class metadatos(View):

    def __init__(self,id):
        self.id=id
        print(id)

    def schema(request,self):
      idm=self.id
      metadatos=Metadatos.objects.get(id=idm)
      print(metadatos)
      con = psycopg2.connect(host="localhost", database="baseuno", user="postgres", password="i076117")
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
               row=cur.fetchone()
            #    while row is not None:
            #        print(row)
            #        row=cur.fetchone()
            #    cur.execute(sql)  
               for row in  cur:
                   print(row)
               data = [row[0] for row in cur.fetchall()]
             
               
            #    return data
               return render(request, 'schema.html', {'schema_met': data})
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')
    
    def tablas(request,self):
      idm=self.id
      metadatos=Metadatos.objects.get(id=idm)
      print(metadatos)
      con = psycopg2.connect(host="localhost", database="baseuno", user="postgres", password="i076117")
      sql=""" SELECT table_catalog,table_schema,table_name,table_type FROM information_schema.tables; """
      try:
               cur = con.cursor()
               cur.execute(sql)
               row=cur.fetchone()
            #    while row is not None:
            #        print(row)
            #        row=cur.fetchone()
            #    cur.execute(sql)  
               for row in  cur:
                   print(row)
               data = [row[0] for row in cur.fetchall()]
             
               
            #    return data
               return render(request, 'tablasbd.html', {'tablas_met': data})
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')

    def reglas(request,self):
      idm=self.id
      metadatos=Metadatos.objects.get(id=idm)
      print(metadatos)
      con = psycopg2.connect(host="localhost", database="baseuno", user="postgres", password="i076117")
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
               row=cur.fetchone()
            #    while row is not None:
            #        print(row)
            #        row=cur.fetchone()
            #    cur.execute(sql)  
               for row in  cur:
                   print(row)
               data = [row[0] for row in cur.fetchall()]
             
               
            #    return data
               return render(request, 'reglas.html', {'reglas_met': metadatos})
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')

    def comentarios(request,self):
      idm=self.id
      metadatos=Metadatos.objects.get(id=idm)
      print(metadatos)
      con = psycopg2.connect(host="localhost", database="baseuno", user="postgres", password="i076117")
      sql="""  SELECT c.table_schema,c.table_name,c.column_name,pgd.description
        FROM pg_catalog.pg_statio_all_tables as st
        inner join pg_catalog.pg_description pgd on (pgd.objoid=st.relid)
        inner join information_schema.columns c on (pgd.objsubid=c.ordinal_position
        and  c.table_schema=st.schemaname and c.table_name=st.relname);"""
      try:
               cur = con.cursor()
               cur.execute(sql)
               row=cur.fetchone()
            #    while row is not None:
            #        print(row)
            #        row=cur.fetchone()
            #    cur.execute(sql)  
               for row in  cur:
                   print(row)
               data = [row[0] for row in cur.fetchall()]
             
               
            #    return data
        
               return render(request, 'comentarios.html', {'comentarios_met': data})
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
        return Metadatos.objects.all().order_by('nombd')
    
    def get_context_data(self, **kwargs):
       context =super().get_context_data(**kwargs)
       context['titulo'] = 'Crear_conexion_bd'
       
       return context


class sch(ListView):

    def schema(request,id):
        metadatos=Metadatos.objects.get(id=id)
        print(metadatos)
        con = psycopg2.connect(host="localhost", database="baseuno", user="postgres", password="i076117")
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
                row=cur.fetchone()
                while row is not None:
                    print(row)
                    row=cur.fetchone()
                cur.execute(sql)  
                #    for row in  cur:
                #        print(row)
                data = [row[0] for row in cur.fetchall()]
                
                
                #    return data
                return render(request, 'schema.html', {'schema_met': data})

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)
        finally:
            if con is not None:
                        con.close()
                        print('Conexión finalizada.')



























def login_view(request):
	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request, user)
		return redirect("/")
	return render(request, "accounts/form.html", {
		"form" : form,
		"title" : "Login",
	})


