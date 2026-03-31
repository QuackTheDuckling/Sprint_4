import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])

    def test_add_new_book_add_two_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 2
    
    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Ужасы')
    ])

    def test_set_book_genre_from_list(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre
    
    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Ужасы')
    ])

    def test_get_book_genre_existing_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Оно', 'Ужасы')
    ])
    
    def test_get_books_with_specific_genre_existing_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Оно')
        collector.set_book_genre(name, genre)

        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби', 'Оно']

    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Экспансия', 'Фантастика')
    ])

    def test_get_books_genre_two_books_different_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Экспансия')
        collector.set_book_genre(name, genre)

        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби':'Ужасы', 'Экспансия':'Фантастика'}
    
    @pytest.mark.parametrize('name, genre', [
        ('Экспансия', 'Фантастика')
        ('Незнайка', 'Комедии')
    ])

    def test_get_books_for_children_one_books_not_in_age_rating(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Экспансия')
        collector.add_new_book('Незнайка')
        collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == ['Экспансия', 'Незнайка']

    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Ужасы')
    ])
    
    def test_add_book_in_favorites_new_book_existing_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Ужасы')
    ])

    def test_delete_book_from_favorites_added_book(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert collector.get_list_of_favorites_books() == []
    
    def test_get_list_of_favorites_books_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_new_book('Экспансия')
        collector.set_book_genre('Экспансия', 'Фантастика')
        collector.add_book_in_favorites('Экспансия')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Экспансия']

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби'])
    
    def test_get_book_genre_not_set_genre(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert collector.get_book_genre(name) == None
    
    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Ужасы')
    ])

    def test_get_books_for_children_one_book_in_age_rating(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == []


