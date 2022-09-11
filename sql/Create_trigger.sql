use Flight_Sys;
#购票时验证是否有余票
drop trigger if exists buy_add;
delimiter //
create trigger buy_add
before insert on ticket for each row
begin
    declare seat_eco smallint(4);
    declare seat_lux smallint(4);
    set seat_eco=(select seats_ceco from timetable
                where flightno=new.flightno
                and deptdate=new.deptdate);
    set seat_lux=(select seats_clux from timetable
                where flightno=new.flightno
                and deptdate=new.deptdate);
    if seat_eco<1 then
        signal sqlstate 'HY000' set message_text='该班次经济舱机票已售罄';
    end if;
    if seat_lux<1 then
        signal sqlstate 'HY000' set message_text='该班次头等舱机票已售罄';
    end if;
    if new.id_passportno not in (select id_passportno from passenger
                                where id_passportno=new.id_passportno )
     then
        signal sqlstate 'HY000' set message_text='请先填写个人信息进行注册';
    end if;
end //

