-- consulta de test para probar
select APELLIDO, DIRECCION from ENFERMO where INSCRIPCION= 10995;
select APELLIDO, FUNCION from PLANTILLA where TURNO='T'; 
select * from PLANTILLA; 
select * from ENFERMO; 
delete from ENFERMO where INSCRIPCION=10995;
ROLLBACK;

insert into DEPT values (88, 'NUEVO', 'NUEVO');
select * from ENFERMO; 
select * from HOSPITAL;
insert into HOSPITAL values (49, 'la luz', 'reina victoria','914-8747','300');

