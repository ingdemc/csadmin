from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import View,ListView
from .models import Metadatos
# from usuarios.models import Usuario
from .forms import metadatosf
import psycopg2
import psycopg2.extras
from django.contrib.auth.decorators import login_required





# Create your views here.

def index(request):
   return render(request, "index.html")

def cont_ment(request):
    

    
    return render(request, 'base.html')

@login_required
def calificacion(request):

    return render(request, 'calificacion.html' )



class ConexionListView(ListView):
    model=Metadatos 
    form_class= metadatosf
    template_name= 'tables.html'
    

    def get_queryset(self):
        id= self.request.user.id
       
        # return Curso.objects.filter(creditos__lte=4)
        return Metadatos.objects.filter(iduser=id)
        
    def get_context_data(self, **kwargs):
       context =super().get_context_data(**kwargs)
       context['titulo'] = 'Crear_conexion_bd'
       
       return context
        
    # def editar(self,request,id):
    #     met = Metadatos.objects.get(id=id)
    #     form= metadatosf(request.POST or None, request.FILES or None, intance=met)
    #     return render(request,self.template_name,{'form':form})
    
    
    
        

@login_required
def crearconexion(request):
     if request.method == 'POST':
        
         form = metadatosf(request.POST)
         if form.is_valid():
            metadatos = form.save(commit=False)
            metadatos.iduser = request.user
            metadatos.save()
            return redirect('/verconexion')
     else:
            form = metadatosf()
            print("error")
         

     return render(request, 'crearconexion.html', {'form': form})



def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def eliminacion(request,id):

    metadatos=Metadatos.objects.get(id=id)
    metadatos.delete()

    return redirect('/verconexion')

def recursividad(request,ide):

    idmet= Metadatos.objects.get(id=ide)
    
    fec= str(idmet.fechacreacion)
    alias= str(idmet.aliasconxion)
    coment=str(idmet.comentariobd)
    hostdb=str(idmet.nomhost)
    port =str(idmet.nompuerto)
    nombd=str(idmet.nombd)
    usuariobd=str(idmet.usuario)
    usuariopass=str(idmet.passw)
    # conection2=(" host="+hostdb+" dbname="+nombd+" port="+port+" user="+usuariobd+" password="+usuariopass)
    csad=str("postgres://"+usuariobd+":"+usuariopass+"@"+hostdb+":"+port+"/"+nombd)
   
    # con = psycopg2.connect (conection2)
    con = psycopg2.connect (csad)
    
    # grapschema= ("postgresql+psycopg2://"+usuariobd+":"+usuariopass+"@"+hostdb+"/"+nombd)
    # graph = create_schema_graph(metadata=MetaData(grapschema),show_datatypes=True,
    # show_indexes=True,show_column_keys=True,rankdir='LR',show_schema_name =True)
    # n_img= 'img/'+nombd+'.png'
    
    
    # graph.write_png('/cargasemantica/static/img/'+nombd+'.png')


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
                
                cur.execute("""SELECT count(*)
    FROM pg_catalog.pg_namespace n
	 WHERE n.nspname !~ '^pg_' AND n.nspname <> 'information_schema'     
   ;""")
                conta= cur.fetchall()
              
                
  ##tablas
                cur = con.cursor()
                cur.execute(""" SELECT  nspname AS schemaname,table_name,COUNT(Table_Name) As NumeroCampos,reltuples::integer,(select pg_catalog.obj_description(oid) 
from pg_catalog.pg_class c 
where c.relname=cols.table_name)
FROM pg_class C
LEFT JOIN pg_namespace N ON (N.oid = C.relnamespace)
JOIN information_schema.columns cols ON (c.relname=cols.table_name)
where nspname NOT IN ('pg_catalog', 'information_schema')
GROUP BY Table_Name,n.nspname,c.relname,c.reltuples
ORDER BY reltuples DESC; """)

#REINDEX DATABASE base_de_datos;
# antes de ejecutar la query, hay que reindexar la base de datos, para que actualice todos los valores y tener una respuesta de la cantidad de datos que existen hasta ese momento.

                tabla= cur.fetchall()
                
                cur.execute(""" SELECT count(*) FROM information_schema.tables where table_schema NOT IN('pg_catalog','information_schema'); """)
                tabla_cont=cur.fetchall()
               
  
  ##indices
                cur = con.cursor()
                cur.execute(""" SELECT 
pg_get_constraintdef(c.oid)                   AS definition,
                                   
     sch.nspname                                   AS "self_schema",
     tbl.relname                                   AS "self_table",

     f_tbl.relname                                 AS "foreign_table"

     
     FROM pg_constraint c
          JOIN pg_class tbl ON tbl.oid = c.conrelid
          JOIN pg_namespace sch ON sch.oid = tbl.relnamespace
         
          LEFT JOIN pg_class f_tbl ON f_tbl.oid = c.confrelid
          LEFT JOIN pg_namespace f_sch ON f_sch.oid = f_tbl.relnamespace
        
     GROUP BY  "self_schema", "self_table", definition, "foreign_table"
     ORDER BY  "definition","self_schema";""")
                regla= cur.fetchall()
                
                cur.execute("""SELECT count(*)
    FROM pg_constraint c
           JOIN pg_class tbl ON tbl.oid = c.conrelid
           JOIN pg_namespace sch ON sch.oid = tbl.relnamespace
           LEFT JOIN pg_class f_tbl ON f_tbl.oid = c.confrelid
           LEFT JOIN pg_namespace f_sch ON f_sch.oid = f_tbl.relnamespace
     ;""")
                regla_cont=cur.fetchall()
               
               
  ##comentarios
                cur = con.cursor()
                cur.execute(""" SELECT 
nspname,relname,
    a.attname as nombre_columna,
    format_type(a.atttypid, a.atttypmod) as tipo,
    a.attnotnull as notnull, 
    com.description as descripcion
FROM pg_attribute a 
 JOIN pg_class pgc ON pgc.oid = a.attrelid
JOIN pg_namespace N ON (N.oid = pgc.relnamespace)
LEFT JOIN pg_description com on 
    (pgc.oid = com.objoid AND a.attnum = com.objsubid)
LEFT JOIN pg_attrdef def ON 
    (a.attrelid = def.adrelid AND a.attnum = def.adnum)
WHERE  nspname NOT IN ('pg_catalog', 'information_schema') AND
relkind='r' AND
a.attnum > 0 AND pgc.oid = a.attrelid

AND NOT a.attisdropped 

ORDER BY relname;""")
                comentario= cur.fetchall()
               
                    
                cur.execute("""SELECT 
count(*)
FROM pg_attribute a 
 JOIN pg_class pgc ON pgc.oid = a.attrelid
JOIN pg_namespace N ON (N.oid = pgc.relnamespace)
LEFT JOIN pg_description com on 
    (pgc.oid = com.objoid AND a.attnum = com.objsubid)
LEFT JOIN pg_attrdef def ON 
    (a.attrelid = def.adrelid AND a.attnum = def.adnum)
WHERE  nspname NOT IN ('pg_catalog', 'information_schema') AND
relkind='r' AND
a.attnum > 0 AND pgc.oid = a.attrelid

AND NOT a.attisdropped 

;""")
                coment_cont=cur.fetchall()






  ##comentarios
                cur = con.cursor()
                cur.execute(""" SELECT n.nspname as "Schema",
  p.proname::text as "Name",
  pg_catalog.pg_get_function_result(p.oid) as "Result data type",
 CASE
  WHEN p.prorettype = 'pg_catalog.trigger'::pg_catalog.regtype THEN 'trigger'
  ELSE 'normal'
 END as "Type"
FROM pg_catalog.pg_proc p
     LEFT JOIN pg_catalog.pg_namespace n ON n.oid = p.pronamespace
WHERE pg_catalog.pg_function_is_visible(p.oid)
      AND n.nspname <> 'pg_catalog'
      AND n.nspname <> 'information_schema'
ORDER BY 1, 2;""")
                func= cur.fetchall()
               
                    
                cur.execute("""SELECT count(*)
FROM pg_catalog.pg_proc p
     LEFT JOIN pg_catalog.pg_namespace n ON n.oid = p.pronamespace
WHERE pg_catalog.pg_function_is_visible(p.oid)
      AND n.nspname <> 'pg_catalog'
      AND n.nspname <> 'information_schema'
;""")
                func_cont=cur.fetchall()








                return render(request, 'metadatos.html', {'schema_met':row, 'metadatos':idmet,'tablas_met': tabla,'reglas_met': regla,'comentarios_met': comentario,'conta':conta,'tabla_cont':tabla_cont,'regla_cont':regla_cont,'coment_cont':coment_cont,'coment':coment,'alias':alias,'fec':fec,'func_cont':func_cont,'func':func,'ide':ide})

    except (Exception, psycopg2.DatabaseError) as error:
                print(error)
    finally:
            if con is not None:
                        con.close()
                        print('Conexión finalizada.')

def detalle_tab(request,id,ide):

    idmet= Metadatos.objects.get(id=ide)
    
    hostdb=str(idmet.nomhost)
    port =str(idmet.nompuerto)
    nombd=str(idmet.nombd)
    usuariobd=str(idmet.usuario)
    usuariopass=str(idmet.passw)
    # conection2=(" host="+hostdb+" dbname="+nombd+" port="+port+" user="+usuariobd+" password="+usuariopass)
    csad=str("postgres://"+usuariobd+":"+usuariopass+"@"+hostdb+":"+port+"/"+nombd)
   
    # con = psycopg2.connect (conection2)
    con = psycopg2.connect (csad)
    
    
    
    
    
    cur = con.cursor()
    
    
    fi=("""SELECT 
pg_get_constraintdef(c.oid)                   AS definition,                              
     sch.nspname                                   AS "self_schema",
     tbl.relname                                   AS "self_table",
     f_tbl.relname                                 AS "foreign_table"
     FROM pg_constraint c
          JOIN pg_class tbl ON tbl.oid = c.conrelid
          JOIN pg_namespace sch ON sch.oid = tbl.relnamespace
         
          LEFT JOIN pg_class f_tbl ON f_tbl.oid = c.confrelid
          LEFT JOIN pg_namespace f_sch ON f_sch.oid = f_tbl.relnamespace
     WHERE  sch.nspname =%s OR tbl.relname =%s
     GROUP BY  "self_schema", "self_table", definition, "foreign_table"
     ORDER BY  "definition","self_schema";   """)
    
    cur.execute(fi ,(id,id))
     
    regla= cur.fetchall()
    
    
    
    cur = con.cursor()
    tip=(""" 
SELECT 
nspname,relname,
    a.attname as nombre_columna,
    format_type(a.atttypid, a.atttypmod) as tipo,
    a.attnotnull as notnull, 
    com.description as descripcion
FROM pg_attribute a 
 JOIN pg_class pgc ON pgc.oid = a.attrelid
JOIN pg_namespace N ON (N.oid = pgc.relnamespace)
LEFT JOIN pg_description com on 
    (pgc.oid = com.objoid AND a.attnum = com.objsubid)
LEFT JOIN pg_attrdef def ON 
    (a.attrelid = def.adrelid AND a.attnum = def.adnum)
WHERE  nspname NOT IN ('pg_catalog', 'information_schema') AND
relkind='r' AND
a.attnum > 0 AND pgc.oid = a.attrelid
AND relname= %s
AND NOT a.attisdropped 
ORDER BY relname;""")
    cur.execute(tip,(id,))
    comentario= cur.fetchall()
    

    return render(request, 'detalle_tabla.html',{'nomtabla': id,'indice':regla, 'coment':comentario,'ide':ide})