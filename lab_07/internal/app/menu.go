package app

import (
	"fmt"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"lab_07/internal/db"
	"os"
)

type App struct {
	database       *db.DB
	optionHandlers []optionHandler
}

func New(dsn string) (*App, error) {
	pureDB, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		return nil, err
	}

	a := &App{
		database: db.NewDB(pureDB),
	}

	a.optionHandlers = []optionHandler{
		{
			name: "Вывести все королевства",
			f:    a.getAllLoyalties,
		},
		{
			name: "Вывести персонажей младше 18",
			f:    a.getOldClients,
		},
		{
			name: "Вывести замки с населением выше 500 и возрастом выше 1900 лет, сортировать по возрасту",
			f:    a.getSortedAttendances,
		},
		{
			name: "Вывести максимальные населения для домов, группированных по состоянию",
			f:    a.getMaxPriceByRating,
		},
		{
			name: "Вывести информацию о персонаже по id",
			f:    a.getMaxPriceByRatingP,
		},
		{
			name: "Прочитать данные о хозяинах из таблицы драконов в формате json",
			f:    a.getFeedbacks,
		},
		{
			name: "Добавить данные о владельцах дракона",
			f:    a.getUpdatedFeedbacks,
		},
		{
			name: "Добавить нового дракона",
			f:    a.getNewFeedbacks,
		},
		{
			name: "Вывести все королевства (классы сущностей)",
			f:    a.getAllLoyalties3,
		},
		{
			name: "Вывести персонажей младше 18 (классы сущностей)",
			f:    a.getJoin3,
		},
		{
			name: "Вставить персонажа",
			f:    a.getInsert3,
		},
		{
			name: "Обновить статус персонажа",
			f:    a.getUpdate3,
		},
		{
			name: "Удалить персонажа по id",
			f:    a.getDelete3,
		},
		{
			name: "Вызвать процедуру изменения id дома персонажа",
			f:    a.getPuzzleUp3,
		},
		{
			name: "Выход",
			f: func() error {
				os.Exit(0)
				return nil
			},
		},
	}

	return a, nil
}

func (a *App) printMenu() {
	fmt.Println("\nMenu:")
	for i, r := range a.optionHandlers {
		fmt.Printf("%02d - %s\n", i, r.name)
	}
}

func (a *App) Run() error {
	for {
		a.printMenu()

		fmt.Println()

		var option int
		fmt.Print("Введите номер пункта меню: ")
		if _, err := fmt.Scan(&option); err != nil {
			fmt.Println(err)
			continue
		}

		if option < 0 || option >= len(a.optionHandlers) {
			fmt.Printf("Error: invalid menu option\n")
			continue
		}

		if err := a.optionHandlers[option].f(); err != nil {
			fmt.Printf("Error: %s\n", err)
			continue
		}

		fmt.Println()
	}
}
