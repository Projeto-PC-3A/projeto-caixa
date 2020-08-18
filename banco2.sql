create database transações;
use transações;

create table usuarios(
id_usuario int not null primary key,
saldo float not null,
criado_data datetime,
atualizado_data datetime
);


create table extrato(
id_extrato int not null auto_increment primary key,
id_conta int not null,
id_origem int not null,
id_destino int not null,
valor decimal(10,2) not null,
tipo varchar(25) not null,
extrato_data datetime not null,
constraint `fk_usuarioExt`
foreign key(`id_conta`)
references transações.usuarios(`id_usuario`)
);

insert into usuarios values(1,3000,'2020/05/06','2020/06/22');

select*from extrato;
