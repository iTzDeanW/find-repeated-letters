def max_word_length(words):

    #پیدا کردن بیشترین طول در بین کلمات 

    max_len = 0
    for w in words:
        if len(w) > max_len:
            max_len = len(w)
    return max_len        

def get_word_with_length(words, length):
    
   # برگرداندن تمام کلماتی که طول مشخصی دارند

   result = []
   for w in words:
     #است length فقط کلماتی که طول آن ها برابر 
        if len(w) == length:
            result.append(w)
   return result

def main():
#تابع اصلی برنامه
    
    #دریافت جمله از کاربر
    sentence = input("Enter a sentence: ")

    # جدا کردن جمله به لیستی از کلمات
    words = sentence.split()

    # پیدا کردن بیشترین طول کلمه
    max_len = max_word_length(words)
    
    # گرفتن همه کلمات با بیشترین طول
    longest_words = get_word_with_length(words, max_len)
    
    # نمایش نتیجه
    print("\nLongest word(s): ")
    for w in longest_words:
        print(f"{w} ({max_len} letters)")
# اجرای برنامه
main()
