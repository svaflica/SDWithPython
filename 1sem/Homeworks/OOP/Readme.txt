Перед Вами - домашнее задание по объектно-ориентированному программированию на Python и всяким прикольным библиотекам.

В файле "Figure.py" Вы найдёте абстрактный класс геометрической фигуры, в папке ".\tests" - открытые тесты к программе (закрытое тестирование предварительно будем проводить мы), для запуска можно использовать pytest (по дефолту решение лежит в solution, но при желании можно поменять внутри кода):
pytest -v -s tests/test.py

Ваша задача состоит в том, чтобы реализовать дочерние классы фигур (будем считать, что все они невырожденные) "Эллипс", "Окружность", "Четырёхугольник", "Прямоугольник", "Квадрат".
Каждый класс должен перегружать методы вычисления площади и периметра, строкового представления фигуры, в котором необходимо указать класс фигуры, площадь, периметр, характерные точки, метод graphFigure, строящий фигуру с помощью matplotlib.

Также Вы могли заметить в папке файл "Figure_data.csv" -  в нём построчно закодированы фигуры в формате: "тип фигуры";<от одной до 4х характерных точек в формате "X:Y" или характерный размер числом с плавающей точкой>;
Для выполнения этого пункта вам предлагается реализовать метод класса constructFromSeries возвращающий экземпляр класса и принимающий объект Series из библиотеки Pandas.
После реализации данного метода для каждого класса необходимо считать данные из файла, распечатать строковые представления каждой фигуры и построить их с помощью метода graphFigure каждого класса

Формат кодирования фигур:
- Эллипс: "ellipse";<center>;<A-axis>;<B-axis>;None
- Окружность: "circle";<center>;<radius>;None;None
- Четырёхугольник: "quadrilateral";<1st vertex>;<2nd vertex>;<3rd vertex>;<4th vertex>
- Прямоугольник: "rectangle";<left-bottom vertex>; <right-up vertex>;None;None
- Квадрат: "square";<left-bottom vertex>; <side length>;None;None
