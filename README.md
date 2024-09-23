# Преобразование сканов pdf в формат текст
Если у вас есть набор сканов в формате PDF, и вы хотите преобразовать их в формат текста, этот репозиторий может быть полезен.
## Установка и настройка

### 1. Клонирование репозитория

Склонируйте репозиторий с помощью следующей команды:

```sh
git clone https://github.com/LLIALLIJLblK pdf_photo_to_text.git
```

### 2. Установка библеотек
pip install -r requirements.txt

```sh
pip install -r requirements.txt
```

### 3. Установите тессеракт себе на устройство

### 4. Укажите путь к файлу который хотите распрасить


### 5. Раскомментируйте строку в в соответствии с вашей OS
длям MacOS 
```sh
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
```
для Liniux
```sh
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
```
для Windows
```sh
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 6. Запустите скрипт
