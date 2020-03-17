/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/2/21 12:41:30                           */
/*==============================================================*/


drop table if exists carts;

drop table if exists category;

drop table if exists comment;

drop table if exists discount;

drop table if exists feedback;

drop table if exists grade;

drop table if exists ident_msg;

drop table if exists indent;

drop table if exists managers;

drop table if exists products;

drop table if exists source;

drop table if exists user;

drop table if exists user_address;

/*==============================================================*/
/* Table: carts                                                 */
/*==============================================================*/
create table carts
(
   carts_id             int not null,
   product_id           int not null,
   user_id              int not null,
   shopnumber           int not null,
   primary key (carts_id)
);

/*==============================================================*/
/* Table: category                                              */
/*==============================================================*/
create table category
(
   category_id          int not null,
   product_id           int not null,
   category_name        varchar(20),
   primary key (category_id)
);

/*==============================================================*/
/* Table: comment                                               */
/*==============================================================*/
create table comment
(
   comment_id           int not null,
   order_id             int,
   comment_time         date,
   comment_content      varchar(200),
   satisfaction         int,
   primary key (comment_id)
);

/*==============================================================*/
/* Table: discount                                              */
/*==============================================================*/
create table discount
(
   discount_id          int not null,
   product_id           int not null,
   discount_price       double,
   primary key (discount_id)
);

/*==============================================================*/
/* Table: feedback                                              */
/*==============================================================*/
create table feedback
(
   feedback_id          int not null,
   user_id              int not null,
   feedback_suggest     varchar(200),
   feedback_content     varchar(200),
   feedback_img         varchar(256),
   feedback_phone       int,
   primary key (feedback_id)
);

/*==============================================================*/
/* Table: grade                                                 */
/*==============================================================*/
create table grade
(
   grade_id             int not null,
   user_id              int not null,
   grade                varchar(10) not null,
   intergration         int not null,
   primary key (grade_id)
);

/*==============================================================*/
/* Table: ident_msg                                             */
/*==============================================================*/
create table ident_msg
(
   product_id           int,
   indent_id            int,
   ident_number         int
);

/*==============================================================*/
/* Table: indent                                                */
/*==============================================================*/
create table indent
(
   indent_id            int not null,
   address_id           int not null,
   indent_time          date not null,
   indent_price         double not null,
   indent_state         Boolean not null,
   primary key (indent_id)
);

/*==============================================================*/
/* Table: managers                                              */
/*==============================================================*/
create table managers
(
   manager_id           int not null,
   account              varchar(10) not null,
   password             varchar(15) not null,
   primary key (manager_id)
);

/*==============================================================*/
/* Table: products                                              */
/*==============================================================*/
create table products
(
   product_id           int not null,
   source_id            int not null,
   product_img          varchar(256),
   product_name         varchar(20) not null,
   product_priceout     double not null,
   product_longname     varchar(20),
   product_makeprice    double not null,
   product_storenum     int not null,
   product_numout       int not null,
   product_time         date not null,
   product_expiretime   date not null,
   primary key (product_id)
);

/*==============================================================*/
/* Table: source                                                */
/*==============================================================*/
create table source
(
   source_id            int not null,
   source_factory       varchar(20) not null,
   source_total         int not null,
   source_price         double not null,
   source_all_price     double not null,
   primary key (source_id)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   user_id              int not null,
   user_img             varchar(256),
   user_name            varchar(20) not null,
   user_password        varchar(20) not null,
   user_phone           int not null,
   user_datetime        date not null,
   isactive             boolean,
   primary key (user_id)
);

/*==============================================================*/
/* Table: user_address                                          */
/*==============================================================*/
create table user_address
(
   address_id           int not null,
   user_id              int not null,
   address              varchar(256) not null,
   telephone            int not null,
   primary key (address_id)
);

alter table carts add constraint FK_Reference_5 foreign key (product_id)
      references products (product_id) on delete restrict on update restrict;

alter table carts add constraint FK_Reference_6 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table category add constraint FK_Reference_7 foreign key (product_id)
      references products (product_id) on delete restrict on update restrict;

alter table comment add constraint FK_Reference_8 foreign key (order_id)
      references indent (indent_id) on delete restrict on update restrict;

alter table discount add constraint FK_Reference_11 foreign key (product_id)
      references products (product_id) on delete restrict on update restrict;

alter table feedback add constraint FK_Reference_9 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table grade add constraint FK_Reference_10 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

alter table ident_msg add constraint FK_Reference_13 foreign key (product_id)
      references products (product_id) on delete restrict on update restrict;

alter table ident_msg add constraint FK_Reference_14 foreign key (indent_id)
      references indent (indent_id) on delete restrict on update restrict;

alter table indent add constraint FK_Reference_3 foreign key (address_id)
      references user_address (address_id) on delete restrict on update restrict;

alter table products add constraint FK_Reference_12 foreign key (source_id)
      references source (id) on delete restrict on update restrict;

alter table user_address add constraint FK_Reference_1 foreign key (user_id)
      references user (user_id) on delete restrict on update restrict;

