cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "r" | grep -E ".{4,}"| grep -v "[^zoniacr]" | wc -l
