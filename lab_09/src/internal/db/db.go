package db

import (
	"database/sql"
	"fmt"
	"gorm.io/gorm"
)

type DB struct {
	db *gorm.DB
}

func New(db *gorm.DB) *DB {
	return &DB{db: db}
}

func rowsToString(rows *sql.Rows) string {
	cols, _ := rows.Columns()
	vals := make([]interface{}, len(cols))
	var res string
	for i := range cols {
		vals[i] = new(interface{})
	}
	for rows.Next() {
		rows.Scan(vals...)
		for _, v := range vals {
			res += fmt.Sprintf("%v ", *v.(*interface{}))
		}
		res += "\n"
	}

	return res
}

func (db *DB) TopLocations() (string, error) {
	rows, err := db.db.Raw("select name, population from public.kingdom order by population desc limit 10;").Rows()
	if err != nil {
		return "", err
	}
	res := rowsToString(rows)

	return res, nil
}

func (db *DB) Insert() (string, error) {
	rows, err := db.db.Raw("insert into public.kingdom (name, main_river , location, population, exist) values ('Западные земли', 'Не известно', 'Эcсос', 1, true);").Rows()
	if err != nil {
		return "", err
	}
	res := rowsToString(rows)
	return res, nil
}

func (db *DB) Update() (string, error) {
	rows, err := db.db.Raw("update public.kingdom set main_river = 'Узкое море' where name = 'Западные земли';").Rows()
	if err != nil {
		return "", err
	}
	res := rowsToString(rows)
	return res, nil
}

func (db *DB) Delete() (string, error) {
	rows, err := db.db.Raw("delete from public.kingdom where population = 1;").Rows()
	if err != nil {
		return "", err
	}
	res := rowsToString(rows)
	return res, nil
}

func (db *DB) Select() (string, error) {
	rows, err := db.db.Raw("select * from public.kingdom").Rows()
	if err != nil {
		return "", err
	}
	res := rowsToString(rows)
	return res, nil
}
