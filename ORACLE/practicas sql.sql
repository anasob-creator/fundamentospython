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
SELECT count(EMP.EMP_NO) as PERSONAS, DEPT.loc
from EMP
FULL join DEPT
ON EMP.DEPT_NO=DEPT.DEPT_NO
group by DEPT.LOC;
-- solo pondremos count(*) si quiero los nulos, 
-- debemos poner count(columna)
-- aquí nunca usaría un full join porque no tendría sentido
-- vamos a mostrar apellido, función, nombre hosp y dirección hosp y nombre sala
SELECT PLANTILLA.APELLIDO, PLANTILLA.FUNCION, HOSPITAL.NOMBRE, HOSPITAL.DIRECCION, SALA.NOMBRE
FROM PLANTILLA
INNER JOIN HOSPITAL
ON PLANTILLA.HOSPITAL_COD=HOSPITAL.HOSPITAL_COD
INNER JOIN SALA
ON HOSPITAL.HOSPITAL_COD=SALA.HOSPITAL_COD
AND PLANTILLA.SALA_COD=SALA.SALA_COD;
-----------------------------------------------------------
-- 1. Seleccionar el apellido, oficio, salario, numero de departamento 
-- y su nombre de todos los empleados cuyo salario sea mayor de 300000
SELECT emp.apellido,  emp.oficio,  emp.salario,  emp.dept_no, dept.dnombre
from EMP
inner join DEPT
on EMP.DEPT_NO=DEPT.DEPT_NO
where emp.salario>300000;
-- 2 Mostrar todos los nombres de Hospital con sus nombres de salas correspondientes.
SELECT HOSPITAL.NOMBRE, SALA.NOMBRE
FROM HOSPITAL
INNER JOIN SALA
ON HOSPITAL.HOSPITAL_COD=SALA.HOSPITAL_COD;
-- 3 Calcular cuántos trabajadores de la empresa hay en cada ciudad.
SELECT COUNT(EMP.EMP_NO) AS TRABAJADORES, DEPT.LOC
FROM EMP
INNER JOIN DEPT
ON DEPT.DEPT_NO=EMP.DEPT_NO
GROUP BY DEPT.LOC;
--Visualizar cuantas personas realizan cada oficio 
--en cada departamento mostrando el nombre del departamento.
SELECT COUNT(*) AS PERSONAS, EMP.OFICIO, DEPT.DNOMBRE
FROM EMP
INNER JOIN DEPT
ON DEPT.DEPT_NO=EMP.DEPT_NO
GROUP BY DEPT.DNOMBRE, EMP.OFICIO;
---Contar cuantas salas hay en cada hospital, 
--mostrando el nombre de las salas y el nombre del hospital.
SELECT COUNT(SALA.SALA_COD) AS NUMSALAS, HOSPITAL.NOMBRE, SALA.NOMBRE
FROM SALA
INNER JOIN HOSPITAL
ON HOSPITAL.HOSPITAL_COD=SALA.HOSPITAL_COD
GROUP BY HOSPITAL.NOMBRE, SALA.NOMBRE;
-- 6 Queremos saber cuántos trabajadores se dieron de alta entre el año 1997
-- y 1998 y en qué departamento.
SELECT COUNT(EMP_NO) AS EMPLEADOS, DEPT_NO, FECHA_ALT
FROM EMP
GROUP BY DEPT_NO, FECHA_ALT
HAVING FECHA_ALT >= '1/01/1997' AND FECHA_ALT <= '12/12/1998';
-- 7- Buscar aquellas ciudades con cuatro o más personas trabajando.
SELECT COUNT(EMP.EMP_NO) AS EMPLEADOS, DEPT.LOC
FROM EMP
INNER JOIN DEPT
ON EMP.DEPT_NO=DEPT.DEPT_NO
GROUP BY DEPT.LOC
HAVING EMPLEADOS>=4;
-- 8 Calcular la media salarial por ciudad.  Mostrar solamente la media para Madrid y Elche.
SELECT AVG(EMP.SALARIO) AS mediaSalarial, dept.loc
from emp 
inner join DEPT
on EMP.DEPT_NO=DEPT.DEPT_NO
group by dept.loc having dept.loc = 'MADRID';
--9 Calcular el salario medio, Diferencia, Máximo y Mínimo 
--de cada oficio. Indicando el oficio y el número de empleados de cada oficio.
SELECT COUNT(EMP_NO) AS EMPLEADOS,
AVG(EMP.SALARIO) AS SALARIOMEDIO, oficio, 
max(salario) as SALARIOMAXIMO
, min(salario) as SALARIOMINIMO
, max(salario) - min(salario) as DIFERENCIA 
from emp group by oficio;
--9 Mostrar los doctores junto con el nombre de hospital 
--n el que ejercen, la dirección y el teléfono del mismo.
SELECT DOCTOR.APELLIDO, HOSPITAL.NOMBRE, HOSPITAL.DIRECCION, 
HOSPITAL.TELEFONO
FROM DOCTOR
INNER JOIN HOSPITAL
ON DOCTOR.HOSPITAL_COD=HOSPITAL.HOSPITAL_COD;
-- 10. Mostrar los nombres de los hospitales junto con el mejor 
-- salario de los empleados de la plantilla de cada hospital.
SELECT MAX(PLANTILLA.SALARIO), 

