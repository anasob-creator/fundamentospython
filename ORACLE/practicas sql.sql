select * from DEPT;
-- mostrar el apellido apellido, oficio, ndept,loc empleados
select EMP.apellido, EMP.oficio, DEPT.dnombre, DEPT.loc
from DEPT
INNER JOIN EMP
ON EMP.DEPT_NO=DEPT.DEPT_NO; 
------ Visualizar el nombre hospital y
------ dirección hosìtal de los doctores
-------------
SELECT hospital.direccion, hospital.nombre, DOCTOR.APELLIDO, DOCTOR.ESPECIALIDAD
from HOSPITAL
inner join DOCTOR
ON HOSPITAL.HOSPITAL_COD=DOCTOR.HOSPITAL_COD;
--- Mostrar el número de personas por cada dpto. 
--- de los empleados
SELECT count(*) as personas, DEPT_NO
from EMP
group by DEPT_NO;
-- ostrar el número de personas por NOMBRE dpto. 
--- de los empleados
SELECT count(*) as personas, DEPT.DNOMBRE
from EMP
inner join DEPT
on EMP.DEPT_NO=DEPT.DEPT_NO
group by DEPT.DNOMBRE;
------ TIPOS DE JOINS - INTEGRIDAD RELACIONAL ---
-- INNER: muestra los res que combinen entre las dos
-- left: muestra los res que combinen entre las dos 
-- y tb los que no combinen de la tabla ida
-- right: muestra los res que combinen entre las dos 
-- y tb los que no combinen de la tabla dcha
-- full: muestra los re de las dos tablas combinen o no
-- cros: muestra el producto cartesiano
-- ejemplos
SELECT distinct DEPT_NO from EMP;
SELECT * from DEPT;
-- Para este ej vamos a crear un empleado sin dpto 
-- ya tenemos un dpto. sin empleado
-- 40-produccion-granada
--1111-aumno-50
-- ahora metemos la consulta inicial con inner join
select EMP.apellido, EMP.oficio, DEPT.dnombre, DEPT.loc
from EMP
INNER JOIN DEPT
ON EMP.DEPT_NO=DEPT.DEPT_NO; 
-- ahora metemos la consulta inicial con left join
select EMP.apellido, EMP.oficio, DEPT.dnombre, DEPT.loc
from EMP
LEFT JOIN DEPT
ON EMP.DEPT_NO=DEPT.DEPT_NO; 
-- ahora metemos la consulta inicial con right join
select EMP.apellido, EMP.oficio, DEPT.dnombre, DEPT.loc
from EMP
RIGHT JOIN DEPT
ON EMP.DEPT_NO=DEPT.DEPT_NO; 
-- ahora metemos la consulta inicial con full join
select EMP.apellido, EMP.oficio, DEPT.dnombre, DEPT.loc
from EMP
FULL JOIN DEPT
ON EMP.DEPT_NO=DEPT.DEPT_NO; 
-- ahora metemos la consulta inicial con cross join
select EMP.apellido, EMP.oficio, DEPT.dnombre, DEPT.loc
from EMP
FULL JOIN DEPT
ON EMP.DEPT_NO=DEPT.DEPT_NO; 
-- visualizar la suma salarial de cada persona de la plantilla por cada nombre de hospital
SELECT sum(PLANTILLA.SALARIO) as SUMASALARIAL, HOSPITAL.NOMBRE
from PLANTILLA
inner join HOSPITAL
on PLANTILLA.HOSPITAL_COD=HOSPITAL.HOSPITAL_COD
group by HOSPITAL.NOMBRE;
-- nº empleados que trabajan por loc
SELECT count(*) as PERSONAS, DEPT.loc
from EMP
inner join DEPT
ON EMP.DEPT_NO=DEPT.DEPT_NO
group by DEPT.LOC;