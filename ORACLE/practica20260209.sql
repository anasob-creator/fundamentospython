-- Insertar todos los valores de la fila (todos los datos de la tabla)
-- esta sintaxix utiliza la tabla como base
select * from HOSPITAL;
-- Con todos los datos
insert into DEPT values (50, 'Python', 'Alcobendas');
select * from DEPT;
-- con algunos valores
insert into DEPT (DEPTO_NO,LOC) values (51, 'Alicante');
-- no son permanentes hasta que diga commit o rollback (guardar o deshacer)
COMMIT;
-- dentro de las consultas de acción existe una herramienta, que son las subconsultas
-- son muy útiles en las consultas de acción y no son recomendables en las de 
-- selección
-- podemos recuperar datos dinámicos de la tabla/s para utlizarlo en acciones
-- Tenemos una nueva persona en plantilla (Lopez) y su función es ENFERMERA
-- de tarde, hospital 22. Insertar este reg. con el max ID disponible de la tabla
-- PLANTILLA. Salario de 150000. 
-- NEcesito saber qué datos tiene esta tabla.
-- Tengo todos los datos menos el id, lo busco
select * from PLANTILLA;
select max(EMP_NO) + 1 from PLANTILLA;
-- 9902
-- aquí inserto
commit;
insert into PLANTILLA
(HOSPTIAL_COD, SALA_COD, APELLIDO, FUNCION,
TURNO, SALARIO, EMPLEADO_NO)
values (22, 6, 'lopez', ENFERMERA, 'T', 150000, (select max(EMP_NO) + 1 from PLANTILLA));
--- Borrado
delete from PLANTILLA;
rollback;
delete from PLANTILLA where APELLIDO='lopez';
-- podemos utilizar subconsultas
-- eliminar toda la plantilla del hospital El Carmen
delete from PLANTILLA where HOSPITAL_COD=
(select HOSPITAL_COD from HOSPITAL where NOMBRE='El Carmen');
-- update
-- modifica 0 1 o varias filas de una tabla.
-- En la misma consulta podemos indicar que deseamos modificar más de una columna
-- sintaxis update TABLA set CAMPO1=VALOR1, CAMPO2=VALOR2
-- Si no ponemos where, modifica todos los regs. de la tabla
-- Subir en 1 el salario de la plantilla (todos)
update PLANTILLA set SALARIO=SALARIO + 1;
-- todos los enfermeros de la plantilla pasarán a ser enfermeras y se les sube el sueldo
-- en 1
update PLANTILLA set FUNCION='ENFERMERA', SALARIO=SALARIO + 1
where FUNCION='ENFERMERO';
-- con subconsultas
-- En el set solo puede devolver un solo valor la subconsulta.
-- ejemplo
-- los empleados de la sala 4 se han puesto en huelga. 
-- Dicen que su compi Karplus cobra más que ellos
-- Modificar el salario de los empleados de la sala 4 poniendo el 
-- mismo salario que Karplus
update PLANTILLA set SALARIO=
(select SALARIO from Plantilla where APELLIDO='diaz b.')
where SALA_COD=4;
SELECT * FROM PLANTILLA;
select * from sala;
-- modificar el turno a mañana a todos los de la plantilla
-- de la sala de psiquiatría
-- como hay varios valores de psiquiatría, porque hay varios hospitales, 
-- hay que poner un IN en lugar de un =
update PLANTILLA set TURNO=
(select TURNO from Plantilla where TURNO='M')
where SALA_COD IN
(select SALA_COD from SALA where NOMBRE='psiquiatria');
-- Ejemplos:
-- 1. insertar un nuevo empleado de la plantilla
--  Su nombre es cabrales, queremos que sea sala 4, turno noche
-- trabajará en el hospital el carmen, 
-- El id el máximo libre
-- 2. una vez insertado elminiar de la plantilla todas las personas
-- que no tienen un hospital asignado.
select * from PLANTILLA;
select max(EMPlEADO_NO) + 1 from PLANTILLA;
-- 9902
commit;
insert into PLANTILLA
(HOSPITAL_COD, SALA_COD, APELLIDO,
TURNO, EMPLEADO_NO)
values (
(select HOSPITAL_COD from HOSPITAL where NOMBRE='El Carmen'), 
4, 'cabrales', 'T', 
(select max(EMPlEADO_NO) + 1 from PLANTILLA));
select * from PLANTILLA;
SELECT * FROM HOSPITAL;
COMMIT;
-- 2. una vez insertado elminiar de la plantilla todas las personas
-- que no tienen un hospital asignado.
delete from PLANTILLA where HOSPITAL_COD is NULL;
-- Si queremos aquellos cuyo código de hospital no esté en la tabla hospital
delete from PLANTILLA where HOSPITAL_COD is NULL OR
HOSPITAL_COD not in (select HOSPITAL_COD from HOSPITAL);
-- Así recuperaríamos también aquellos que tengan un código que no existe en HOSPITAL
-- POr último tenemos una instrucción para eliminar todos los registros de una tabla de la forma 
-- más rápida, porque no tienen ROLLBACK. 
-- TRUNCATE TABLE NOMBRETABLA
//delete from HOSPITAL;
--ROLLBACK;
-- rollback  recupera el delete, lo que no pasaría con el truncate
--select * from HOSPITAL;
-------------------------------------------------------------------
- 1.  Dar de alta con fecha actual al empleado José Escriche Barrera como 
--programador perteneciente al departamento de producción.  
--Tendrá un salario base de 70000 pts/mes y no cobrará comisión.
SELECT * FROM PLANTILLA;
select * from EMP;
(select max(EMP_NO) + 1 from EMP);
SELECT * FROM dept;
------ 1. 
insert into EMP
(APELLIDO, OFICIO, SALARIO, FECHA_ALT, COMISION, EMP_NO)
values ('josé escriche barrera', 'PROGRAMADOR', 70000, '09/02/26', 0,
(select max(EMP_NO) + 1 from EMP))
where DEPT_NO = (select from DEPT where DNOMBRE='PRODUCCIÓN'); 
-- 40
-- 2 Se quiere dar de alta un departamento de informática situado en Fuenlabrada (Madrid).
insert into DEPT
(DNOMBRE, LOC, DEPT_NO)
values ('INFORMATICA', 'FUENLABRADA (MADRID)',
(SELECT max(DEPT_NO) + 10 FROM DEPT));
-- 3. El departamento de ventas, por motivos peseteros, se traslada a Teruel, realizar dicha modificación.
update DEPT set loc='TERUEL'
where DNOMBRE='VENTAS';
-- 4. En el departamento anterior (ventas), se dan de alta dos empleados: 
-- Julián Romeral y Luis Alonso.  
--Su salario base es el menor que cobre un empleado, y 
--cobrarán una comisión del 15% de dicho salario.
SELECT * FROM PLANTILLA;
select * from EMP;
(select max(EMP_NO) + 1 from EMP);
SELECT * FROM dept;
----------
insert into EMP
(EMP_NO, APELLIDO, SALARIO, COMISION, DEPT_NO)
values
((select max(EMP_NO) + 1 from EMP), 'Julián Romeral', 
(select min(SALARIO) from EMP), 
((select min(SALARIO) from EMP)*0.15),
(select DEPT_NO from DEPT where DNOMBRE='VENTAS'));
insert into EMP
(EMP_NO, APELLIDO, SALARIO, COMISION, DEPT_NO)
values
((select max(EMP_NO) + 1 from EMP), 'Luis Alonso', 
(select min(SALARIO) from EMP), 
((select min(SALARIO) from EMP)*0.15),
(select DEPT_NO from DEPT where DNOMBRE='VENTAS'));
--- vamos a borrar los duplicados
delete from EMP where APELLIDO='Julián Romeral'; 
delete from EMP where APELLIDO='Luis Alonso';
delete from EMP where APELLIDO='josé escriche barrera'; 
-- 5. Modificar la comisión de los empleados de la empresa, 
-- de forma que todos tengan un incremento del 10% del salario.
update EMP set SALARIO=(SALARIO+(SALARIO*0.10));
select * from EMP;
---
-- 6. Incrementar un 5% el salario 
--de los interinos de la plantilla 
-- que trabajen en el turno de noche.
SELECT * FROM PLANTILLA; 
update PLANTILLA set SALARIO=
(select SALARIO from Plantilla where TURNO='N' AND
where FUNCION='INTERINO';

