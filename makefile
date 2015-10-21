FILES :=                              \
	.gitignore						  \
	makefile						  \	
	apiary.apib 					  \
	IDB1.log 						  \
	model.html						  \
	models.py 						  \
	tests.py 						  \
	UML.pdf							

check:
	@not_found=0;                                 \
	for i in $(FILES);                            \
	do                                            \
		if [ -e $$i ];                            \
		then                                      \
			echo "$$i found";                     \
		else                                      \
			echo "$$i NOT FOUND";                 \
			not_found=`expr "$$not_found" + "1"`; \
		fi                                        \
	done;                                         \
	if [ $$not_found -ne 0 ];                     \
	then                                          \
		echo "$$not_found failures";              \
		exit 1;                                   \
	fi;                                           \
	echo "success";

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