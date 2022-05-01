mkdir data
for ((i = 1; i <= $1; i++)); do
    dd if=/dev/zero of=./data/${i}.bin bs=${2}k count=1 &>/dev/null
done
