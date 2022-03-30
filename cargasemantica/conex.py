
import psycopg2
import psycopg2.extras
# from database.connection import add_conection


def select_by_id():
      con = psycopg2.connect(host="localhost", database="cargasemantica", user="postgres", password="i076117")
      sql="""SELECT c.table_schema,c.table_name,c.column_name,pgd.description FROM pg_catalog.pg_statio_all_tables as st   inner join pg_catalog.pg_description pgd on (pgd.objoid=st.relid) inner join information_schema.columns c on (pgd.objsubid=c.ordinal_position     and  c.table_schema=st.schemaname and c.table_name=st.relname);"""
      try:
               cur = con.cursor()
               cur.execute(sql)
               data = cur.fetchall()
               return data
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')



def select_by_ruler():
      con = psycopg2.connect(host="localhost", database="cargasemantica", user="postgres", password="i076117")
          
      sql="""
     SELECT c.conname                                 AS constraint_name,                                   
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
               data = cur.fetchall()
               return data
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')




def schema():
      con = psycopg2.connect(host="localhost", database="cargasemantica", user="postgres", password="i076117")
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
               data = cur.fetchall()
               return data
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')



def comentario():
      con = psycopg2.connect(host="localhost", database="cargasemantica", user="postgres", password="i076117")
      sql="""SELECT c.table_schema,c.table_name,c.column_name,pgd.description
FROM pg_catalog.pg_statio_all_tables as st
inner join pg_catalog.pg_description pgd on (pgd.objoid=st.relid)
inner join information_schema.columns c on (pgd.objsubid=c.ordinal_position
and  c.table_schema=st.schemaname and c.table_name=st.relname);"""
      try:
               cur = con.cursor()
               cur.execute(sql)
               data = cur.fetchall()
               return data
      except (Exception, psycopg2.DatabaseError) as error:
               print(error)
      finally:
          if con is not None:
                    con.close()
                    print('Conexión finalizada.')





