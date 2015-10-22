clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  tests.tmp

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

model.html: models.py
	pydoc3 -w models

IDB1.log:
	git log > IDB1.log

test.tmp: test.py
	coverage3 run    --branch test.py >  test.tmp 2>&1
	coverage3 report -m                      >> test.tmp
	cat test.tmp