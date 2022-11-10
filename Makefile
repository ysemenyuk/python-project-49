install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

make lint:
	poetry run flake8 brain_games
