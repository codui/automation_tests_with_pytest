import pytest


@pytest.mark.temp
def test_file_creation_and_reading(tmp_path):
    # ! tmp_path - это объект pathlib.Path, указывающий на временную папку
    print(f"Временная папка: {tmp_path}")

    # Создать поддиректорию внутри временной папки
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    # Создать путь к файлу
    file_path = data_dir / "my_file.txt"

    # Записать в файл текст с помощью удобного метода pathlib
    file_path.write_text("Hello from tmp_path!")

    # Проверить что файл существует и содержит правильный текст
    assert file_path.exists()
    assert file_path.read_text() == "Hello from tmp_path!"
