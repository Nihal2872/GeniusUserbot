import random
from AdityaHalder import CMD_HELP, bot
from AdityaHalder.events import register
from time import sleep
from AdityaHalder.cmdhelp import CmdHelp
from AdityaHalder import BREND_MENTION

SOZLER = ["‘Kendini beğenmiş insanları severim. Kimsenin beğenmediği bir şeyi sevmek ayrıcalıktır’ derler, peki siz ?",
"Canım sen arkamdan konuşuyorsun. Ama ben pek arkama bakmıyorum, haberin olsun !",
"Bəs deyirdin ölərəm sənsiz ?",
"Şövkət Ələkbərova deyiləm, amma məndə çox gün görmədim.",
"Eyyub Yaqubov deyiləm, amma yamanca yorulmuşam.",
"Mikayıl Müşfiq deyiləm, amma ana olmaz bizə hər bir ‘yavrum’ deyən gözəldən.",
"Rəşid Behbudov deyiləm, amma səni unutmaram mən son nəfəsdə.",
"Duman deyiləm, ama seni kendime sakladım.",
"Köhnə dostunuz əşya olsaydı , hansı əşya olardı ?",
"Numaranızı almam 2 dk’mı alır.",
"193 + 198 = 200 deyil, bilirdiz bunu ?",
"Ciddi soruşuram, makyaj etmədən evdən çıxan qız var, yəni ?",
"Adəm&Lilit’ə baxmayan bir mən qalmışam, bir də Adəm&Lilit",
"Evliliyə neçə nömrəli avtobus gedir ?",
"Ben güneşsem sen aysın, benim doğduğum yerde batarsın.",
"Sana gitme demeyeceğim. Ama gitme, Lavinia."
"Milletin hayatı sürprizlere dolu, bizimki sinsilerle.", 
"100 verib adam ettiysek, 0la çarpar yok ederiz."
"Ben senin karakterine laf etmedim. Ama olsa zevkle ederim.",
"Salam, necəsən, qaqai ?",
"Tez gəlsən, sənə party verəcəm",
"Aloooo . Səsimm gəlirrrr?",
"Salam . Siz ona nə çox bənzəyirsiz 🤔",
"Ekoş sen misin?",
"Ekoş olmaq bi ayrıcalıktır",
"Getsən, gedirsənsə sevgili yar , ancaq unutma",
"Tez gəldə bəs . Darıxdıq🚬",
"Deyilənə görə quşlar uçur . Səncə, düzdü ?🤔",
"Bəli , bəli , o sənsən",
"Küçələrə su səpmişəm, ama sən gəlmirsən",
"Ürəyimdən sənə party vermək keçir 😅 . Gəl, tez ol",
"Ən böyük səhvinin nə olduğunu düşünürsən ?",
"Hamıvızdan narazı, özümədn razı mənəm.",
"Ay tənli qadıın, adının yanında soyadıım",
"Brend Userbot işlədək 💙",
"Qrupda davadı, tez ol gəl",
"Gəl, domino oynamağa gedirik",
"Səni sevdiyim qədər daşı sevsəm , çiçək açardı , nankör",
"Aldırma, gönül aldırma",
"Affet beni akşamüstü",
"İki saatdır səni tag edən var . Gəl bax gör kimdi ?",
"Dedilər ki, sənin fərqli məharətin var . Göstər də bəs",
"Allahın emri, Peyğamberin kabriyle kızınızı oğlumuza istiyoruz",
"1 aprel deyiləm, amma məni görən yalan deyir", 
"Bahar gəldi, sən gəlməz oldun",
"Gəl, qaytar eşqimi",
"Rübabə Muradova deyiləm, amma unuda bilmirəm",
"Necə unudum səni ?"
"Fikrindən gecələr yata bilmirəm..",
"Bu gün nəsə qəmgin görünürsən",
"Hiç mi demedin, ona da yazık diye",
"İkimiz də itirdik, sən məni, mən zamanımı.",
"Kabul olan tek duamsın.."
"Bize yeni düşmanlar lazım, eskileri hayranımız oldu",
"Yarım kalmış bir film yoktur, o film o kadardır",
"Bana attığın kazıkları saklıyorum, döndüğünde oturacak yerin olsun diye",
"Beni silahla öldüremezsin, istersen bir de gülmeyi dene !",
"Arkamdan konuşub beste yapacağına, yüzüme konuşta duet yapalım",
"Bir şəxs var. Deyir ki, sizi tanıyır. Gəlib baxın" , 
"Bəs sən 32 hərfdən hansına aşiq oldun ?" , 
"Ürəyi və beyni olmayan heyvan hansıdır ?",
"Çünki belə gözəldi o",
"Bu şəhər insanları öldürür, axı, səncə, nədən ?",
"Kusurlar güzellikdir, delilik ise zevk. Ve tamamen saçma biri olmak, tamamen sıkıcı biri olmaktan iyidir",
"Bi' çocuğun ruhunu öldürmek de cinayettir",
"Aklımda seninle başbaşayız",
"Vursalar ölmezdim, güldüler kandım",
"Oysa mən sənə yuxum da belə xəyanət etməmişəm",
"Dinləməkdən bezmədiyin mahnı hansıdır ?",
"Aueslər yoxsa madaqaskarlı hamilə iquanaların barmağı ?",
"Kar yağdığında mikroplar ölürmüş, iyi misin?",
"Ara sıra kullan o beynini, yan etkisi yokmuş.",
"Telefonu kendinden daha akıllı olan insanlar var.",
"Bazı insanlar hep ‘KAPTAN’ olurlar, söz konusu ‘DÜMEN ÇEVİRMEK’ olunca.",
"Lütfen insan taklidi yapma, yakışmıyor.",
"İkinizi də Allah öldürsün, səni də, Hitleri də.",
"Yalansa, fransuzki ilan vursun dilünnən.",
"Sizi bura yığmaqda məqsədim odur ki, sizinlə işləmək çox çətindi.",
"Sizdən adam olmuyubx olmuyacaq.",
"Sənə əjdaha lazımdır ?",
"Uşaqlar da deyir ki, atamız işə gedib.",
"Mavi rəngi görə bilən yeganə quş hansıdır ?",
"Yerimi deyim, qaçaraq gəlirsən ?",
"Sevən ölməz demişlər, Leyla ilə Məcnun harada ?",
"Mən az danışım, sən çox anla, olar mı ?",
"Quru duanı burax, ağac istəyən toxum əkər.",
"İşığı heç kim kor qədər sevə bilməz.",
"Yılan sadece derisini değiştirir, huyunu asla.", 
"Hazırlaşın, elçiliyə gedirik 🥳",
"Hayatına böyle girsem, napabilirsin ki ?",
"Təsadüflərin ən gözəli sənin qarşıma çıxmağın idi",
"Qısqanma məni, onların hamı olduğu yerdə sən hərşeyimsən.",
"Onu hələ də sevəcəksən ?",
"Səni sevmək çox gözəl idi. Amma mən bu gün o hisslə vədalaşdım.",
"Qadınlara görə kişilərə etibar etmək olmaz. Kişilərə görə isə qadınlara etibar etmək olmaz. Bəs, səncə ?",
"Hər şeyi başa düşdüm, amma gözlərimin içinə baxıb üzüvü çevirib niyə getdin ?",
"Sən də təkcə mənim yadıma düşdün",
"Camaatın şəhərdə axtardığı mənzərəni, mən sənin gözlərində tapmışdım",
"Sevməyib, sevgi nədir ? bilə bilsəydi sevərdi",
"Çox gözləyəcəm ?",
"Naz eləmə mənə, az elə",
"aaa, gör kimi görürəm, sən də burdasan ?",
"Hal - hazırda sahib olduğunuz en gerçək dostunuz kimdir ?",
"Mənim səndən uzaqlarda yamandı halım, necəsən ?",
"Hər gün yaxşı olmaya bilər, amma hər günün içində yaxşı birşey vardır",
"Milyonlarca insan var dünyada, amma mən səndə tutulub qaldım"]

@register(outgoing=True, groups_only=True, pattern="^.rdtag(?: |$)(.*)")
async def tagone(tag):
    chat = await tag.get_input_chat()
    a_=0
    await tag.delete()
    async for i in bot.iter_participants(chat):
        if a_ == 500:
                break
        a_+=5
        await tag.client.send_message(tag.chat_id, f"[{i.first_name}](tg://user?id={i.id}) **{random.choice(SOZLER)}**")
        sleep(2)
    

CmdHelp('randomtag').add_command(
    'rdtag', None, 'Random sözlərlə tağ edər \n @MUCVE_M tərəfindən hazırlanıb'
).add()
