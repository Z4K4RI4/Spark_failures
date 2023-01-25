size=10000000000
while [ $size -gt 0 ]; do 
    openssl rand -base64 $((size > 1000000 ? 1000000 : size)) >> bigfile.txt
    size=$((size - 1000000))
done
