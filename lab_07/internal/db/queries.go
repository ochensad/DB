package db

import "encoding/json"

// Вывести все королевства
func (db *DB) GetAllLoyalties() ([]map[string]interface{}, error) {
	var l []map[string]interface{}
	if result := db.db.Table("kingdom").Find(&l); result.Error != nil {
		return nil, result.Error
	}

	return l, nil
}

// Вывести персонажей, которые младше 18
func (db *DB) GetOldClients() ([]map[string]interface{}, error) {
	var c []map[string]interface{}
	if result := db.db.Table("character").Find(&c, "age < 18"); result.Error != nil {
		return nil, result.Error
	}

	return c, nil
}

// Вывести замки с населением выше 500 и возрастом выше 1900 лет, сортировать по возрасту
func (db *DB) GetSortedAttendances() ([]map[string]interface{}, error) {
	var a []map[string]interface{}
	if result := db.db.Table("castle").Order("age").Find(&a, "population > ? and age > ?", 500, 1900); result.Error != nil {
		return nil, result.Error
	}

	return a, nil
}

func (db *DB) GetMaxPriceByRating() ([]map[string]interface{}, error) {
	var a []map[string]interface{}
	if result := db.db.Table("house").Select("exist, max(followers) as max_p").Group("exist").Find(&a); result.Error != nil {
		return nil, result.Error
	}

	return a, nil
}

func (db *DB) GetMaxPriceByRatingP(id int) ([]map[string]interface{}, error) {
	var a []map[string]interface{}

	if result := db.db.Table("character").Select("name, age,sex").Find(&a, "id_character = ? ", id); result.Error != nil {
		return nil, result.Error
	}

	return a, nil
}

func (db *DB) GetFeedbacks() ([]string, error) {
	var a []string

	if result := db.db.Table("dragons").Select("masters_id").Find(&a); result.Error != nil {
		return nil, result.Error
	}

	return a, nil
}

func (db *DB) GetUpdatedFeedbacks(f []string) ([]string, error) {
	for i, v := range f {
		var j DragonsJSON
		if err := json.Unmarshal([]byte(v), &j); err != nil {
			return nil, err
		}

		j.MastersId = "i have no masters!"

		fStr, err := json.Marshal(j)
		if err != nil {
			return nil, err
		}

		f[i] = string(fStr)
	}

	return f, nil
}

func (db *DB) GetNewFeedbacks(f []string, j DragonsJSON) ([]string, error) {
	fJSON, err := json.Marshal(j)
	if err != nil {
		return nil, err
	}

	f = append(f, string(fJSON))

	return f, nil
}

func (db *DB) GetAllLoyalties3() ([]Kingdom, error) {
	var l []Kingdom
	if result := db.db.Table("Kingdom").Find(&l); result.Error != nil {
		return nil, result.Error
	}

	return l, nil
}

func (db *DB) GetJoin3() ([]House, error) {
	var l []House

	if result := db.db.Table("character").Select("name, age, sex").Joins("join house on house.id_house = character.id_character").Limit(10).Scan(&l); result.Error != nil {
		return nil, result.Error
	}

	return l, nil
}

func (db *DB) GetInsert(c Character) error {
	if result := db.db.Table("character").Create(&c); result.Error != nil {
		return result.Error
	}

	return nil
}

func (db *DB) GetUpdate(i int, p2 int) error {
	if result := db.db.Table("character").Where("id_character = ?", i).Update("age", p2); result.Error != nil {
		return result.Error
	}

	return nil
}

func (db *DB) GetDelete(l int) error {
	if result := db.db.Table("character").Where("id_character = ?", l).Delete(&Character{}); result.Error != nil {
		return result.Error
	}

	return nil
}

func (db *DB) GetCount() (int, error) {
	var l int

	result := db.db.Table("character").Select("max(id_character) as i").Find(&l)
	if result.Error != nil {
		return 0, result.Error
	}

	return l, nil
}

func (db *DB) GetPuzzleUp(up int, id int) error {
	result := db.db.Raw("call ChangePersonStatus(?, ?);", up, id).Scan(nil)
	if result.Error != nil {
		return result.Error
	}

	return nil
}
