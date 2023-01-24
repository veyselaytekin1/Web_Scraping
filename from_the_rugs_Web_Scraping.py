#pip install Pillow
#pip install requests
#pip install selenium  ## Selenium kullama sebebimiz tarayicimizi otomatik hale getiriyor

from selenium import webdriver   
from selenium.webdriver.common.by import By #bu kücük resimlerin class'larini almak icin
import requests
import io   ##fotoyu bytlarla saklamak ile ilgili 
from PIL import Image
import time


PATH = '//Users//veyselaytekin//Desktop//Data_Science//1_PYTHON_VE_LIBRARY//Web_Scraping//chromedriver'
#exec'te olabilir sonu
# bu PATH bizim Chrome icin indirdigimiz dosyanin yolu,yapacagimiz islemleri Chromeda yapmak icin 
#burda / tek slash isareti vardi, hata cikmamasi icin iki tan eyaptik ama neden hata alacagimizi bilmiyorum



wd = webdriver.Chrome(PATH)  #bu bize crome sayfasini aciyor, ve icine hangi url verirsen asagidaki kod ile onu veriyor


def get_images_from_google(wd, delay, max_images):   #max_images maksimum kac resim indirecegimiz ile ilgili, wd=yukarida tarayici ile ilgili
    def scroll_down(wd):   #ekranlari asagi kaydirma islemi icin
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay) #fotolari teker teker secerken kac saniye sonra islemleri devam ettirecegi ile ilgili sanki
    url = "https://www.google.com/search?q=the+rugs&rlz=1C5CHFA_enDE1027DE1027&sxsrf=AJOqlzWgqkW-ZVEZrA3wnHJ2UTMS8NlRXQ:1674552577717&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjqtrW88t_8AhWSSPEDHSfzBT0Q_AUoAnoECAUQBA&biw=1440&bih=789&dpr=2"
    #b bizim resimlerini almak istedigimiz sayfanin url'si

    wd.get(url)    # galiba bu sayfayi Croma yükleyecek

    image_urls = set()
    skips = 0

    while len(image_urls) + skips < max_images:   #burda def icine max_images saiysi yazacagiz, bu yazdigimiz sayi kadar resim gelmesini istiyoruz
        scroll_down(wd)     #sayfanin sonuna kadar gitmesi icin

        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")  #bu galiba kücük resimöler üzerinde dolasacak ve onlarin urlsini almak icin olabilir, bu kod ise kücük resimlerin class adi

        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue


            images = wd.find_elements(By.CLASS_NAME, "n3VNCb")    # bu ise google images'lerde orta boy resimlere tiklayinca sagda büyük resim ciktigindaki incele'deki class codu
            for image in images:
                if image.get_attribute('src') in image_urls:   #bu eger orta boy resimlerden biri eger kaynagi yoksa onu almamasi icin, and http ilede kaynaginin olup olmadigini garantiliyoruz
                    max_images += 1
                    skips += 1
                    break

                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")
    return image_urls



#get_images_from_google(wd, 2, 10)   
#wd.quit()  #chrome'u bir kere acmasi icin ve islem bittigine pencereyi kapatacaktir



def download_image(download_path, url, file_name):    # file_name:resimleiri kaydetmek istedigim dosyanin adi,dowland_path= galiba fotoyu baska bir yere indirmek istrsek buraya bir yol yazabiliriz
    try:
        image_content = requests.get(url).content   #url ile istek almamizi sagliyor,content bize görüntünün icerigini verecek
        image_file = io.BytesIO(image_content)    #io fotonun byte'larla ilgili oldugu kisimla ilgili bisey ama tam olarak ne bakmadaim halen, BytesIO dosyayi bellekte saklamak ile ilgili dedi
        image = Image.open(image_file)   #buda fotoyu acmamiz icin
        file_path = download_path + file_name   #görüntüyü kaydetmek icin dosya yolu olusturuyorum

        with open(file_path, "wb") as f:   #foto acmak icin,'wb=write ve byte anlaminda, resmi f ye kaydedecegim dedi
            image.save(f, "JPEG")
        print("Success")


    except Exception as e:   #bu e ile kisaltma yapti,ve asagida bastirack
        print('FAILED -', e)


# bu kod ile requests ile fotoy almak icin bir request gönderiyoruz, content ile görüntünün icerigini aliyoruz
# io.BytesIO ile foto kisa süreli depolaniyor,open ile fotoyu aciyor ve within altindaki yerde fotoyu kaydediyor




urls = get_images_from_google(wd, 1, 6)

for i, url in enumerate(urls):
    download_image("imgs/", url, str(i) + ".jpg")


wd.quit()    








# download_image('',image_url, 'caimasCollection.jpg')  #dowland_pate birsey yazmadi, oldugu yere insin dedi


# bu kodu yoruma aldim cünkü her calistirdigimda kaydetmesin
#su an sadece buraya kadarki yazisima göre, iki foto linki koyup indirdim, ikincisini indirdikten sonra ilki 
# silindi, yani her foto icin, hem fonksiyon cagirikenki icine yazdigimiz jpgli ismini,hemde image_url
#olan yeride degistirmeliyiz

# örnegin url yi eksik yazinca kod calisti ama söyle bir cikti verdi, yani kod durmadi
#FAILED cannot identify image file <_io.BytesIO object at 0x7fda893202c0>