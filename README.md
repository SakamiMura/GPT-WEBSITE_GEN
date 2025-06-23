## Działanie Aplikacji 
Ten program służy do generowania kodu HTML na podstawie treści artykułu, korzystając z API OpenAI. 
Program pobiera do api artykuł zapisany w pliku tekstowym (`artykulbase.txt`) oraz prompt użytkownika, a nastepnie konwertuje go na surową sekcję body kodu HTML.
Ostatecznie zapisuje wynik do pliku `artykul.html`.

## Wymagania
1. Python 3.11 lub wyższy.
2. Konto OpenAI oraz klucz API.
3. Zainstalowana biblioteka `openai`

## Instrukcja Uruchomienia

Klonowanie repozytorium: W pierwszej kolejności sklonuj repozytorium na swoje lokalne środowisko. W terminalu lub wierszu poleceń wpisz:
git clone <URL_do_repozytorium>

Otwórz plik Gen_HTML.py i wprowadź swój unikalny klucz API OpenAI.

1. Jeśli masz inny artykuł na bazie którego chcesz stworzyć fragment kodu HTML, możesz wprowadzić go teraz do pliku artykulbase.txt, jeśli nie możesz posłużyć się tym, który już jest.
2. Uruchom plik Gen_HTML.py za pomocą np. Visual Studio Code lub PyCharm. 
3. W pliku artykul.html powinien pojawić się świeżo wygenerowany kod zawierający szkielet artykułu wraz ze znacznikami HTML.
4. Aby wyświetlić go w przeglądarce, możesz skorzystać z pliku podglad.html, wklej w wyznaczonej sekcji całość kodu jaki uzyskałeś w pliku artukul.html.

Gotowe:)



