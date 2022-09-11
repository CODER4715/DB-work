use Flight_Sys;
#航班查询视图
drop view if exists search_tickets;
create view search_tickets
    as
    select airlinename,t1.flightno as flightno,t1.deptdate as deptdate,flight_status,
            depttime,arvtime,seats_ceco,seats_clux,dept,arv,eco_price,lux_price
    from
    (select airlinename,flightno,deptdate,depttime,arvtime,seats_ceco,
            seats_clux,airportname as dept,flight_status
    from timetable natural join flight natural join airline left outer join
            airport on flight.dept_airport=airport.airportno
    ) as t1
    left outer join
    (
    select flightno,deptdate,airportname as arv
    from timetable natural join flight natural join airline left outer join
            airport on flight.arv_airport=airport.airportno
    ) as t2
    on t1.flightno=t2.flightno and t1.deptdate=t2.deptdate
    left outer join price on t1.flightno=price.flightno and t1.deptdate=price.deptdate;


#购票信息查询视图
drop view if exists book_tickets;
create view book_tickets 
as
select * from ticket natural join passenger
