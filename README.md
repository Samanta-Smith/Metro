Микросервис с API для проверок станций метро.

    На вход подается список станций метро, происходит сравенение исходных данные с данными из источника [https://api.hh.ru/metro/1](https://api.hh.ru/metro/1) и выводятся

    1. Станции без отличий (полное совпадение)

    2. Новые станции (те, которых нет в базе hh)

    3. Удаленные станции (те, которых нет в запросе)

    Данные из [https://api.hh.ru/metro/1](https://api.hh.ru/metro/1) получаются  вызовом API.

    **На вход:** POST /api/v1/metro/verificate/

        [
        	"Каховская",
        	"Баррикадная",
        	...
        ]

    **На выход:**

        {	
        	"unchanged": [...],
        	"updated": [...],
        	"deleted": [...]
        }