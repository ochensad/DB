package db

// import (
// 	"time"
// )

type Religion struct {
	ID          int `gorm:"primaryKey,autoIncrement"`
	Name        string
	Type     	string
	Clergy  	string
	Propagation string
	Followers 	int
}

type Kingdom struct {
	ID    		int `gorm:"primaryKey,autoIncrement"`
	Name        string
	MainRiver   string
	Location    string
	Population  int
	Exist    	bool
}

type Organization struct {
	ID    		int `gorm:"primaryKey,autoIncrement"`
	Name        string
	Type        string
	Location    string
	State  		string
	Followers    int
}

type House struct {
	ID    		int `gorm:"primaryKey,autoIncrement"`
	Name        string
	Blazon      string
	Motto    	string
	Followers  	int
	Exist    	bool
	IDKingdom   int
}

type Castle struct {
	ID    		int `gorm:"primaryKey,autoIncrement"`
	Name        string
	Type      	string
	Population 	int
	Age  		int
	IDHouse   	int
	IDReligion  int
	IDKingdom   int
}

type Character struct {
	ID    		int `gorm:"primaryKey,autoIncrement"`
	Name        string
	Sex      	string
	Culture 	string
	Title 		string
	Motherland 	string
	Age  		int
	Alive 		bool
	IDHouse  	int
	IDReligion  int
}

type Organ_and_charac struct {
	IDOrganization  int
	IDCharacter    	int
	State 		bool
	Years_in  		int
}

type DragonsJSON struct {
	ID      int `gorm:"primaryKey,autoIncrement"`
	Name   string
	CurMasterID int
	MastersId    string `json:"masters,omitempty"`
}

