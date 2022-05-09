create database main;
use main;

# Create tables
create table quiz (
	quizid int not null auto_increment,
    quiz_question varchar(255),
    quiz_answer boolean,
    primary key (quizid)
);
create table fact (
	factid int not null auto_increment,
    fact varchar(255),
    source varchar(255),
    primary key (factid)
);
create table twitter_users(
	user_no int auto_increment,
	display_name varchar(255),
    acct_name varchar(255),
    description varchar(1200),
    followers int,
    following int,
    verified varchar(10),
    age int,
    tweets_per_day float,
    default_image varchar(10),
    real_acct varchar(10),
    primary key (user_no)
);
create table wordcloud (
	source varchar(100),
    handle varchar(100),
    wordcount varchar(10000)
);
create table wc_sources (
	source varchar(100),
	description varchar(255)
);

# Add constraints to wordcloud table
alter table wordcloud drop column wc_id;
alter table wordcloud add column wc_id int not null auto_increment primary key first;
alter table wordcloud add constraint source_fk foreign key (source) references wc_sources(source);

# Add constraints to wc_sources table
alter table wc_sources add primary key (source);
insert into wc_sources values ('fake_news', 'Word counts from the FakeNewsNet dataset');
insert into wc_sources values ('twitter', 'Tweets pulled via the Twitter API');

commit;