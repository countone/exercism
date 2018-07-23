words={ 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
      6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
      11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
      15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
      19 : 'nineteen', 20 : 'twenty',
      30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
      70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}

def say(number):
  
  if -1<number<=999:

    if number<100:
      if number<21 or number%10==0:
        return words[number]
      elif number/10!=0:
        return words[number//10*10]+'-'+words[number%10]
    else:
      if number%100==0:
        return words[number//100]+' hundred'
      else:
        return words[number//100]+' hundred and '+say(number%100)

  elif 999<number<=999999:
    if number%1000==0:
      in_words=say(number//1000)+' thousand'
    elif number%1000<100:
      in_words=say(number//1000)+' thousand and '+say(number%1000)
    else:
      in_words=say(number//1000)+' thousand '+say(number%1000)
  
  elif 999999<number<=999999999:
    if number%1000000==0:
      in_words=say(number//1000000)+' million'
    elif number%1000000<100:
      in_words=say(number//1000000)+' million and '+say(number%1000000)
    else:
      in_words=say(number//1000000)+' million '+say(number%1000000)
  
  elif 999999999<number<=999999999999:
    if number%1000000000==0:
      in_words=say(number//1000000000)+' billion'
    elif number%1000000000<100:
      in_words=say(number//1000000000)+' billion and '+say(number%1000000000)
    else:
      in_words=say(number//1000000000)+' billion '+say(number%1000000000)
  else:
    raise ValueError('ValueError')

  return in_words