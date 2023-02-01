package app

import (
	"bufio"
	"fmt"
	"lab_07/internal/db"
	"os"
	"strings"
)

var feedbacks []string

type optionHandler struct {
	name string
	f    func() error
}

func printSlice[T any](s []T) {
	fmt.Println("RESULT:")
	for i, e := range s {
		fmt.Printf("%d: %+v\n", i, e)
	}
}

func (a *App) getAllLoyalties() error {
	result, err := a.database.GetAllLoyalties()
	if err != nil {
		return err
	}

	printSlice(result)

	return nil
}

func (a *App) getSortedAttendances() error {
	result, err := a.database.GetSortedAttendances()
	if err != nil {
		return err
	}

	printSlice(result)

	return nil
}

func (a *App) getOldClients() error {
	result, err := a.database.GetOldClients()
	if err != nil {
		return err
	}

	printSlice(result)

	return nil
}

func (a *App) getMaxPriceByRating() error {
	result, err := a.database.GetMaxPriceByRating()
	if err != nil {
		return err
	}

	printSlice(result)

	return nil
}

func (a *App) getMaxPriceByRatingP() error {
	var price int

	fmt.Print("Введите id: ")

	if _, err := fmt.Scan(&price); err != nil {
		return err
	}

	result, err := a.database.GetMaxPriceByRatingP(price)
	if err != nil {
		return err
	}

	printSlice(result)

	return nil
}

func (a *App) getFeedbacks() error {
	result, err := a.database.GetFeedbacks()
	if err != nil {
		return err
	}

	printSlice(result)
	feedbacks = result

	return nil
}

func (a *App) getUpdatedFeedbacks() error {
	result, err := a.database.GetUpdatedFeedbacks(feedbacks)
	if err != nil {
		return err
	}

	printSlice(result)
	feedbacks = result

	return nil
}

func (a *App) getNewFeedbacks() error {
	fmt.Print("Введите имя дракона: ")
	stuff, err := bufio.NewReader(os.Stdin).ReadString('\n')
	if err != nil {
		return err
	}
	stuff = strings.TrimSpace(stuff)

	var id_h int
	fmt.Print("Введите id владельца: ")
	if _, err := fmt.Scan(&id_h); err != nil {
		return err
	}

	fmt.Print("Введите id предыдущих владельцев: ")
	park, err := bufio.NewReader(os.Stdin).ReadString('\n')
	if err != nil {
		return err
	}
	park = strings.TrimSpace(park)
	id, err := a.database.GetCount()
	if err != nil {
		return err
	}
	j := db.DragonsJSON{
		ID:      int(id) + 1,
		Name:   stuff,
		CurMasterID: id_h,
		MastersId:    park,
	}

	result, err := a.database.GetNewFeedbacks(feedbacks, j)
	if err != nil {
		return err
	}

	printSlice(result)
	feedbacks = result

	return nil
}

func (a *App) getAllLoyalties3() error {
	result, err := a.database.GetAllLoyalties3()
	if err != nil {
		return err
	}

	printSlice(result)

	return nil
}

func (a *App) getJoin3() error {
	result, err := a.database.GetJoin3()
	if err != nil {
		return err
	}

	printSlice(result)

	return nil
}

func (a *App) getInsert3() error {
	var name string
	fmt.Print("Введите имя: ")
	if _, err := fmt.Scan(&name); err != nil {
		return err
	}
	name = strings.TrimSpace(name)

	var sex string
	fmt.Print("Введите пол: ")
	if _, err := fmt.Scan(&sex); err != nil {
		return err
	}
	sex = strings.TrimSpace(sex)

	var culture string
	fmt.Print("Введите культуру: ")
	if _, err := fmt.Scan(&culture); err != nil {
		return err
	}
	culture = strings.TrimSpace(culture)

	var title string
	fmt.Print("Введите титул: ")
	if _, err := fmt.Scan(&title); err != nil {
		return err
	}
	title = strings.TrimSpace(title)

	var motherland string
	fmt.Print("Введите родину: ")
	if _, err := fmt.Scan(&motherland); err != nil {
		return err
	}
	motherland = strings.TrimSpace(motherland)

	var age int
	fmt.Print("Введите возраст: ")
	if _, err := fmt.Scan(&age); err != nil {
		return err
	}

	var id_h int
	fmt.Print("Введите id дома: ")
	if _, err := fmt.Scan(&id_h); err != nil {
		return err
	}

	var id_r int
	fmt.Print("Введите id религии: ")
	if _, err := fmt.Scan(&id_r); err != nil {
		return err
	}

	id, err := a.database.GetCount()
	if err != nil {
		return err
	}

	var alive bool = true

	c := db.Character{
		ID:          int(id) + 1,
		Name:		name,
		Sex:    	sex,
		Culture: 	culture,
		Title: 		title,
		Motherland: 	motherland,
		Age:  		age,
		Alive: 		alive,
		IDHouse:  	id_h,
		IDReligion:  id_r,
	}

	err = a.database.GetInsert(c)
	if err != nil {
		return err
	}

	fmt.Printf("Вставлен: %v\n", c)

	return nil
}

func (a *App) getUpdate3() error {
	var id int
	fmt.Print("Введите id: ")
	if _, err := fmt.Scan(&id); err != nil {
		return err
	}

	var alive int
	fmt.Print("Введите новый возраст: ")
	if _, err := fmt.Scan(&alive); err != nil {
		return err
	}

	err := a.database.GetUpdate(id, alive)
	if err != nil {
		return err
	}

	return nil
}

func (a *App) getDelete3() error {
	var login int
	fmt.Print("Введите id: ")
	if _, err := fmt.Scan(&login); err != nil {
		return err
	}

	err := a.database.GetDelete(login)
	if err != nil {
		return err
	}

	return nil
}

func (a *App) getPuzzleUp3() error {
	var up int
	fmt.Print("Введите id персонажа: ")
	if _, err := fmt.Scan(&up); err != nil {
		return err
	}

	var id_h int
	fmt.Print("Введите новое id дома: ")
	if _, err := fmt.Scan(&id_h); err != nil {
		return err
	}

	err := a.database.GetPuzzleUp(up, id_h)
	if err != nil {
		return err
	}

	return nil
}
