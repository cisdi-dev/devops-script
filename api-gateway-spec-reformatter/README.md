Script ini mengotomasi formating api spec sesuai dengan yang diterima oleh google API Gateway

Untuk menjalankan scrip ini pertama buat sebuah `.env.${environment_name}` dengan value sebagai berikut
```
API_URL="https://${URL_API_GATEWAY}"
```

kemudian jalankan script dengan perintah berikut:
```
./reformatter.sh $PATH_SWAGGER_YAML_FILE $ENVIRONMENT
```
perintah tersebut akan mengenerate sebuah yaml file yang digunakan untuk membuat `api-configs` pada Google API Gateway