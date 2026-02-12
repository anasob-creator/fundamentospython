-- consulta de test para probar
-- Para mirar el tipo de dato que tenemos se puede mirar
-- en la estructura o bien más rápido es esta instrucción
desc HOSPITAL;
select APELLIDO, DIRECCION from ENFERMO where INSCRIPCION= 10995;
select APELLIDO, FUNCION from PLANTILLA where TURNO='T'; 
select * from PLANTILLA; 
select * from ENFERMO; 
select * from EMP; 
delete from ENFERMO where INSCRIPCION=10995;
ROLLBACK;
insert into DEPT values (88, 'NUEVO', 'NUEVO');
select * from ENFERMO; 
select * from HOSPITAL;
insert into HOSPITAL values (49, 'la luz', 'reina victoria','914-8747','300');
select APELLIDO, OFICIO, DEPT_NO from EMP where DEPT_NO=20;
update DEPT set loc='TERUEL'
where DNOMBRE='VENTAS';
update EMP set SALARIO=SALARIO+10
where OFICIO='DIRECTOR';
update PLANTILLA set SALARIO=SALARIO+10
where HOSPITAL_COD='19';
select * from DOCTOR;
select max(DOCTOR_NO) as MAXIMO from DOCTOR;
