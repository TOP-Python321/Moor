drop database if exists mus_library;

create database mus_library;

use mus_library;

create table performers (
    id smallint unsigned primary key auto_increment,
    name varchar(50) not null unique
);

create table styles (
    id tinyint unsigned primary key auto_increment,
    style varchar(45) not null unique
);

create table publishers (
    id smallint unsigned primary key auto_increment,
    publisher varchar(100) not null unique,
    country varchar(45) not null
);

create table music_collection (
    id smallint unsigned primary key auto_increment,
    album_title varchar(45) not null unique,
    output_date date not null,
    performer_id smallint unsigned not null,
    style_id tinyint unsigned not null,
    publisher_id smallint unsigned not null,
    constraint performers
        foreign key (performer_id) references performers (id)
        on delete cascade 
		on update cascade,
	constraint styles
		foreign key (style_id) references styles (id)
		on delete cascade 
		on update cascade,
	constraint publishers
		foreign key (publisher_id) references publishers (id)
		on delete cascade 
		on update cascade
);

create table songs (
	id int unsigned primary key auto_increment,
	song varchar(45) not null,
	collection smallint unsigned not null,
	style tinyint unsigned not null,
	duration decimal(4, 2) not null,
	constraint music_collection
		foreign key (collection) references music_collection (id)
		on delete cascade 
		on update cascade,
	constraint styles_songs
		foreign key (style) references styles (id)
		on delete cascade 
		on update cascade
);