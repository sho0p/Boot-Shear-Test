for i in $(seq 1 10);
do
	mv raw_$i.csv raw_$i_broken.csv
	python remove_errors.py raw_$i_broken.csv raw_$i.csv
done
