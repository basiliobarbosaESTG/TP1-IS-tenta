#queries para realizar o insert, update e delete
insert_sp = """CALL public.insert_xmlfile(
    %s::character varying(255), 
    %s::xml, 
    %s::date
);"""

get_last = """SELECT id, filename, date FROM public.xmldata WHERE id = (SELECT last_value from xmldata_id_seq);"""

#update_sp = """CALL public.update_xmlfile(
    #%s::integer,
    #%s::character varying(255), 
    #%s::xml, 
    #%s::date
#);"""

get_row = """SELECT * FROM public.xmldata WHERE id = %s;"""

delete_sp = """CALL public.delete_xmlfile(
    %s::integer
);"""