alter table Character
add constraint correct_sex check (sex = 'м' or sex = 'ж');

alter table Castle
add constraint correct_age check (age >= 1),
add constraint correct_population check (population >= 1);

alter table House
add constraint correct_followers check (followers >= 1);

alter table Organization
add constraint correct_followers check (followers >= 1);

alter table Kingdom
add constraint correct_population check (population >= 1);

alter table Religion
add constraint correct_followers check (followers >= 1);