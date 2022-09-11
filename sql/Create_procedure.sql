use Flight_Sys;

#删除航班
delimiter // 
drop procedure if exists delete_flight;
create procedure delete_flight(flightno_ char(7))
    begin
        if exists(select * from ticket where flightno=flightno_) then
            signal sqlstate 'HY000' set message_text='请先退回机票再执行删除操作';
            elseif exists(select * from flight where flightno=flightno_) then
            delete from flight where flightno=flightno_;
            else signal sqlstate 'HY000' set message_text='找不到航班信息';
        end if;
    end //

#删除班次
delimiter //
drop procedure if exists del_banci;
create procedure del_banci(IN FlightNo_ char(7), IN DeptDate_ integer)
    begin
        if exists(select * from timetable where (FlightNo_=flightno and DeptDate_=deptdate)) then
        delete from timetable where (FlightNo_=flightno and DeptDate_=deptdate);
        else signal sqlstate'HY000' set message_text='找不到该班次';
        end if;
    end //


#增加班次与班次修改
drop procedure if exists modify_timetable;
delimiter //
create procedure modify_timetable(IN FlightNo_ char(7), IN DeptDate_ integer, IN DeptTime_ integer, 
IN ArvTime_ char(5), IN status_ varchar(4), IN eco_ integer, IN lux_ integer,IN ecoPrice_ FLOAT,IN luxPrice_ FLOAT)
    begin
        declare eco_have integer;
        declare lux_have integer;
        declare eco_total integer;
        declare lux_total integer;
        if exists(select * from timetable where (FlightNo_=flightno and DeptDate_=deptdate)) then
		set eco_have=(select seats_ceco from timetable
                where (flightno=FlightNo_ and deptdate=DeptDate_));
        set lux_have=(select seats_clux from timetable
                where (flightno=FlightNo_ and deptdate=DeptDate_));
        set eco_total=(select seats_eco from timetable
                where (flightno=FlightNo_ and deptdate=DeptDate_));
        set lux_total=(select seats_lux from timetable
                where (flightno=FlightNo_ and deptdate=DeptDate_));
		if eco_<(eco_total-eco_have) then
            signal sqlstate 'HY000' set message_text='改动无效，若改动后经济舱将有部分已购票旅客无座位，请先退回这部分票再进行操作！';
		end if;
        if lux_<(lux_total-lux_have) then
            signal sqlstate 'HY000' set message_text='改动无效，若改动后头等舱将有部分已购票旅客无座位，请先退回这部分票再进行操作！';
		end if;
        update timetable
            set depttime=DeptTime_, arvtime=ArvTime_, seats_eco=eco_, seats_lux=lux_, flight_status=status_,
            seats_ceco=eco_-(eco_total-eco_have), seats_clux=lux_-(lux_total-lux_have)
            where (flightno=FlightNo_ and deptdate=DeptDate_);
        update price
            set eco_price=ecoPrice_,lux_price=luxPrice_
            where (flightno=FlightNo_ and deptdate=DeptDate_);
        else 
            insert into timetable(FlightNo, DeptDate, DeptTime, ArvTime, flight_status, seats_eco,
            seats_ceco, seats_lux, seats_clux) 
            VALUES (FlightNo_, DeptDate_ , DeptTime_, ArvTime_, status_, eco_, eco_, lux_, lux_);
            insert into price(flightno, deptdate, eco_price, lux_price)
            VALUES (FlightNo_, DeptDate_ , ecoPrice_, luxPrice_);
        end if;
	end//


#购票
delimiter // 
drop procedure if exists buyT ;
create procedure buyT (IN FlightNo_ char(7), IN DeptDate_ integer, IN ID_PassportNo_ varchar(30),IN seat_ integer)
    begin
		declare seat integer;
        if exists(select * from timetable where FlightNo_=flightno and DeptDate_=deptdate) then
            if seat_=1 then
            set seat=(select seats_ceco from timetable
                where flightno=FlightNo_ and deptdate=DeptDate_);
            insert into ticket(flightno,deptdate,seat,id_passportno,seat_class)
                values(FlightNo_,DeptDate_,seat,ID_PassportNo_,'1');
            set seat=seat-1;
            update timetable
            set seats_ceco=seat
                where flightno=FlightNo_ and deptdate=DeptDate_;
            else
            set seat=(select seats_clux from timetable
                where flightno=FlightNo_ and deptdate=DeptDate_);
            insert into ticket(flightno,deptdate,seat,id_passportno,seat_class)
                values(FlightNo_,DeptDate_,seat,ID_PassportNo_,'2');
            set seat=seat-1;
            update timetable
            set seats_clux=seat
                where flightno=FlightNo_ and deptdate=DeptDate_;
            end if;
        else signal sqlstate 'HY000' set message_text='找不到航班信息！';
        end if;
    end //


#退票
delimiter //
drop procedure if exists ticket_back;
create procedure ticket_back(FlightNo_ char(7), DeptDate_ integer, ID_PassportNo_ varchar(30), IN seat_ integer)
    begin
			declare seat integer;
        if exists(select * from ticket where flightno=flightno_) then 
            delete from ticket where (id_passportno=ID_PassportNo_ and FlightNo_=flightno and DeptDate_=deptdate);
            if seat_=1 then
            set seat=(select seats_ceco from timetable where flightno=FlightNo_ and deptdate=DeptDate_);
            set seat = seat + 1;
            update timetable
            set seats_ceco=seat
                where (flightno=FlightNo_ and deptdate=DeptDate_);
            else
            set seat=(select seats_clux from timetable where flightno=FlightNo_ and deptdate=DeptDate_);
            set seat = seat + 1;
            update timetable
            set seats_clux=seat
                where (flightno=FlightNo_ and deptdate=DeptDate_);
            end if;
		else signal sqlstate 'HY000' set message_text='找不到购票信息，请确认查询信息';
        end if;
    end //


#中国人信息注册
delimiter // 
drop procedure if exists information_updating_cn;
create procedure information_updating_cn(enname_ varchar(50),cnname_ varchar(20),nationality_ varchar(20),
tel_ bigint(11),id_passportno_ varchar(50),ethnic_ char(5),sex_ varchar(2))
    begin
        if nationality_ != '中国' then
            signal sqlstate 'HY000' set message_text='国籍填写错误，非中国籍人士请到foreigner板块填写';
        end if;
        if exists (select * from passenger where id_passportno=id_passportno_) then
            update passenger set tel=tel_ where id_passportno=id_passportno_;
            update passenger set nationality=nationality_ where id_passportno=id_passportno_;
            update passenger set enname=enname_ where id_passportno=id_passportno_;
        else insert into passenger(id_passportno,tel,nationality,enname)
                values (id_passportno_,tel_,nationality_,enname_);
        end if;
        if exists (select * from chinese where id_passportno=id_passportno_) then
                update chinese set cnname=cnname_ where id_passportno=id_passportno_;
                update chinese set ethnic=ethnic_ where id_passportno=id_passportno_;
                update chinese set sex=sex_ where id_passportno=id_passportno_;
            else insert into chinese(id_passportno,cnname,ethnic,sex)
                values(id_passportno_,cnname_,ethnic_,sex_);
        end if;
    end //


#外国人信息注册
delimiter // 
drop procedure if exists information_updating_fr;
create procedure information_updating_fr(enname_ varchar(50),nationality_ varchar(20),tel_ bigint(11),
id_passportno_ varchar(50),visano_ varchar(100),sex_ varchar(8))
    begin
        if nationality_='中国' then
            signal sqlstate 'HY000' set message_text='国籍填写错误，中国籍人士请到Chinese板块填写';
        end if;
        if exists (select * from passenger where id_passportno=id_passportno_) then
            update passenger set tel=tel_ where id_passportno=id_passportno_;
            update passenger set nationality=nationality_ where id_passportno=id_passportno_;
            update passenger set enname=enname_ where id_passportno=id_passportno_;

        else insert into passenger(id_passportno,tel,nationality,enname)
                values (id_passportno_,tel_,nationality_,enname_);
        end if;
        if exists (select * from foreigner where id_passportno=id_passportno_) then
                update foreigner set visano=visano_ where id_passportno=id_passportno_;
                update foreigner set sex=sex_ where id_passportno=id_passportno_;
            else insert into foreigner(id_passportno,visano,sex)
                values(id_passportno_,visano_,sex_);
        end if;
    end //