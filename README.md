# Ozbend_Engraving_Internal
Engraving_Internal - часть проекта Ozbend_Jewelry_Render для рендера гравировки отдельно от мешей.

Установка
-

- Скачать zip-файл с дистрибутивом
- В Blender: User Preferences - Add-ons - Install from File - указать скачанный архив


# Использование
Алгоритм работы, подготовки файлов, наименования материалов и мешей какой же, как в исходном Ozbend_Jewelry_Render_v2.

**Изменения:**

- движок рендера Blender Render (internal)
- Всем мешам без гравировки назначается прозрачный материал
- Всем мешам с гравировкой назначается материал текстуры с прозрачным фоном

**Результат рендера:**

Одна гравировка "висящая в воздухе", без мешей.

# Подготовка сцены

В сцене должны присутствовать 2 материала с именами:

- Trans - материал полностью прозраный (назначается мешам без гравировки)
- Gravi - материал текстуры на прозрачном фоне (назначается мешам с гравировкой)

**Прозрачный фон на рендере:**

окно Properties - вкладка Render:

панель Output - установить формат PNG (RGBA)

панель Shading - установить Alpha = Transparent

**Прозрачный материал:**

окно Properties - вкладка Material - для материала меша:

панель Transparencу - установить галочку и поставить Alpha = 0

**Текстура с прозрачным фоном**

материал - так же,как для прозрачного материала

панель Texture - создать новую текстуру в слоте 0 (первый слот)

type = Image or Movie

панель Image - добавить нужную текстуру (формат png, прозрачный фон)

панель Influence - отметить галочку Alpha

панель Mapping - установить Coordinates = UV
