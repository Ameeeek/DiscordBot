import discord
from discord.ext import commands
import os 
from keep_alive import keep_alive
client = discord.Client()
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
  activity=discord.Activity(type=discord.ActivityType.watching, name='UWOHGH😭')
  await client.change_presence(activity=activity)
  print('bot {0.user} udah nyala coek'.format(client))

@client.command(name='version')
async def version(context):

  myEmbed = discord.Embed(title="Stress Bot", description="StressBot For You DegenerateWeebs", color=0x00ff00)
  myEmbed.add_field(name="version code: ", value="v1.1", inline=False)
  myEmbed.add_field(name="date released: ", value="7/24/2021", inline=False)
  myEmbed.set_footer(text='use it wisely u degenerate')
  myEmbed.set_author(name="Amek")
  await context.message.channel.send(embed=myEmbed)
@client.event
async def on_message(pesan):
  if pesan.author == client.user:
    return

  if pesan.content.startswith('$ID'):
    await pesan.channel.send(f'pilih tipe stressmu!\n 1.ringan\n 2.berat\n 3.Gws (sumpah GWS bro)\n 4.Waifu diklem\n 5.halu\n 6.rsj\n 7.SEGGGGGGGGGGGGGSSSSSSSSS\n 8.Extreme\n 9.Suap')
  if pesan.content.startswith('$EN'):
    await pesan.channel.send(f'Choose your Stress Type!\n 1. I NEED TO BREED\n 2. GOD DAMNIT')
  if pesan.content.startswith('$1id'):
        channel = pesan.channel
        await channel.send('tulis namanya dulu coek')

        def check(m):
            waifu = m.content
            return m.content == waifu and m.channel == channel

        msg = await client.wait_for('message', check=check)
        waifu = msg.content
        await channel.send(f'{waifu} {waifu} {waifu} ❤️ ❤️ ❤️ WANGI WANGI WANGI WANGI HU HA HU HA HU HA, aaaah bau rambutnya {waifu} aku mau nyiumin aroma wanginya {waifu} AAAAAAAAH ~ Rambutnya.... aaah rambutnya juga pengen aku elus-elus ~~ AAAAAH {waifu} keluar pertama kali di anime juga manis ❤️ ❤️ ❤️ banget AAAAAAAAH {waifu} AAAAA LUCCUUUUUUUUUUUUUUU............{waifu} AAAAAAAAAAAAAAAAAAAAGH ❤️ ❤️ ❤️apa ? {waifu} itu gak nyata ? Cuma HALU katamu ? nggak, ngak ngak ngak ngak NGAAAAAAAAK GUA GAK PERCAYA. {waifu} ITU NYATA NGAAAAAAAAAAAAAAAAAK PEDULI !! GUA GAK PEDULI SAMA KENYATAAN POKOKNYA GAK PEDULI. ❤️ ❤️ ❤️ {waifu} gw ... di laptop ngeliatin gw, {waifu} .. kamu percaya sama aku ? aaaaaaaaaaah syukur  aku gak mau merelakan {waifu} aaaaaah ❤️ ❤️ ❤️ YEAAAAAAAAAAAH GUA MASIH PUNYA {waifu} SENDIRI PUN NGGAK SAMA AAAAAAAAAAAAAAH'.format(msg))
  if pesan.content.startswith('$2id'):
        channel = pesan.channel
        await channel.send('tulis namanya dulu coek')

        def check(m):
            waifu = m.content
            return m.content == waifu and m.channel == channel

        msg = await client.wait_for('message', check=check)
        waifu = msg.content
        await channel.send(f'Bro, gue gemeteran. GUE GEMETERAN Gue gak pernah mau berkembang biak dengan siapapun lebih daripada seorang. {waifu} Badannya yang cakep, pinggul seksi dari seorang BIDADARI. Jujur aja, sakit hati kalau tau KENYATAANNYA gue GAK AKAN PERNAH BISA BUAT KAWIN SAMA DIA, ngewarisin gen gue lewat dia, dan ngebiarin dia ngelahirin anak yang sempurna dari gue.Gue rela ngelakuin APAPUN demi kesempatan buat bikin {waifu} hamil. A P A P U N. Dan gue bener-bener gk bisa terima kenyataan. Kenapa Authornya rela bikin suatu hal yang sempurna kyk dia? Buat ngegoda kita? NGETAWAIN KITA DI DEPAN MUKA?SUMPAH BRO, GUE UDAH BENER BENER GAK TAHAN...'.format(msg))
  if pesan.content.startswith('$3id'):
        channel = pesan.channel
        await channel.send('tulis namanya dulu coek')

        def check(m):
            waifu = m.content
            return m.content == waifu and m.channel == channel

        msg = await client.wait_for('message', check=check)
        waifu = msg.content
        await channel.send(f'Buruan, panggil gue SIMP, ato BAPERAN. ini MURNI PERASAAN GUE. Gue pengen genjot bareng {waifu}. Ini seriusan, suaranya yang imut, mukanya yang cantik, apalagi badannya yang aduhai ningkatin gairah gue buat genjot {waifu}. Setiap lapisan kulitnya pengen gue jilat. Saat gue mau crot, gue bakal moncrot sepenuh hati, bisa di perut, muka, badan, sampai lubang burit pun bakal gue crot sampai puncak klimaks. Gue bakal meluk dia abis gue moncrot, lalu nanya gimana kabarnya, ngrasain enggas bareng saat telanjang. Dia bakal bilang kalau genjotan gue mantep dan nyatain perasaannya ke gue, bilang kalo dia cinta ama gue. Gue bakal bilang balik seberapa gue cinta ama dia, dan dia bakal kecup gue di pipi. Terus kita ganti pakaian dan ngabisin waktu nonton film, sambil pelukan ama makan hidangan favorit. Gue mau {waifu} jadi pacar, pasangan, istri, dan idup gue. Gue cinta dia dan ingin dia jadi bagian tubuh gue. Lo kira ini copypasta? Kagak cok. Gue ngetik tiap kata nyatain prasaan gue. Setiap kali elo nanya dia siapa, denger ini baik-baik : DIA ISTRI GUE. Gue sayang {waifu}, dan INI MURNI PIKIRAN DAN PERASAAN GUE'.format(msg))
  
  if pesan.content.startswith('$4id'):
        channel = pesan.channel
        await channel.send('tulis namanya dulu coek')

        def check(m):
            waifu = m.content
            return m.content == waifu and m.channel == channel

        msg = await client.wait_for('message', check=check)
        waifu = msg.content
        await channel.send(f'Sejujurnya gw ga nyangka ama tindakan lo yg ga dewasa begini Kita udh temenan dri kecil ,melalui berbagai kenangan ,tapi sikaplo begini ke gw ,ga habis pikir. Padahal sudah berjanji tidak mengusik hubungan satu sama lain lagi ,tapi maksud tindakan mu sekarang ini apa? Tiba tiba di pagi bangun tidur lu make Pp {waifu}. Lu kira lucu begitu? Make waifu pp org seenaknya? Ngeklaim pula bangsad maksudnya apa apaan coba . Pertemanan dari kecil kita ga dihargai sama sekali. \nGw tunggu klarifikasi lo'.format(msg))
  
  if pesan.content.startswith('$5id'):
        channel = pesan.channel
        await channel.send('tulis namanya dulu coek')

        def check(m):
            waifu = m.content
            return m.content == waifu and m.channel == channel

        msg = await client.wait_for('message', check=check)
        waifu = msg.content
        await channel.send(f'Usiaku 22 tahun. Aku sangat mencintai {waifu}, aku punya semua Figurine dan wallpapernya. Aku berdoa setiap malam dan berterima kasih atas segala hal yang telah ia berikan kepadaku. \"{waifu} adalah cinta\" aku bilang \"{waifu}adalah Tujuan Hidupku\". Temanku datang ke kamarku dan berkata \"HALU LU !!\". Aku tau dia cemburu atas kesetiaanku kepada ${waifu}. Lalu kukatakan padanya \"BACOT !!\". Temanku menampol kepalaku dan menyuruhku untuk tidur. Kepalaku sakit dan aku menangis. Aku rebahan di kasur yang dingin, lalu ada sesuatu yang hangat menyentuhku. Ternyata {waifu} datang ke dalam kamarku, Aku begitu senang bertemu {waifu}. Dia membisikan ke telingaku, \"Kamu adalah impianku\" Dengan tangannya dia meraih diriku. Aku melebarkan pantatku keatas demi {waifu}. Dia menusukan sesuatu kedalam Anggusku. begitu sakit, tapi kulakukan itu demi {waifu}. Aku ingin memberikan kepuasan kepada {waifu}. Dia meraum bagaikan singa, disaat dia melepaskan cintanya kedalam Anggusku. Temanku masuk kekamarku dan berkata \"....... Anjing\". {waifu} melihat temanku dan berkata \" Semua sudah berakhir\" Dengan menggunakan kemampuannya Stellar Restoration {waifu} pergi meninggalkan kamarku. \"{waifu} itu cinta\" \"{waifu} itu kehidupan\"'.format(msg))
  
  if pesan.content.startswith('$6id'):
        channel = pesan.channel
        await channel.send('tulis namanya dulu coek')

        def check(m):
            waifu = m.content
            return m.content == waifu and m.channel == channel

        msg = await client.wait_for('message', check=check)
        waifu = msg.content.upper()
        await channel.send(f'{waifu}, INJAK GW {waifu}, INJAK GW SEKUAT TENAGAMU , TATAP AKU DENGAN TATAPAN SERAM MU {waifu}, HINA AKU, LUDAHI AKU {waifu}, CACI MAKI AKU DENGAN TATAPAN TAJAM MU {waifu}, AI LAP UUU {waifu} I LOVE U SOOOOOOOOOOOO MUUUUCCCCHHHHH {waifu} HU HA HU HA WANGY WANGY!!!!'.format(msg))

  if pesan.content.startswith('$7id'):
        channel = pesan.channel
        await channel.send('tulis namanya dulu coek')

        def check(m):
            waifu = m.content
            return m.content == waifu and m.channel == channel

        msg = await client.wait_for('message', check=check)
        waifu = msg.content.upper()
        await channel.send(f'WOOOAAGHHSHSHSHWKSJSIHSSUSSDHG {waifu} CROT BANGET SUMPAH PENGEN BERSETUBUH SAMA {waifu} SAMPE GAK BISA DIRI 😭😭😭😭😭😭 SEEEGGGGSSSSS😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭'.format(msg))

  if pesan.content.startswith('$1en'):
        channel = pesan.channel
        await channel.send('write the name first')

        def check(m):
            waifu = m.content
            return m.content == waifu and m.channel == channel

        msg = await client.wait_for('message', check=check)
        waifu = msg.content.upper()
        await channel.send(f'I NEED TO BREED {waifu} I NEED HER TO MOTHER MY CHILDREN I NEED TO FILL HER WOMB I WANT EVERY SINGLE DROP EVERY LAST SINGLE SPERM CELL MY BODY EVER PRODUCES TO BE IN {waifu}\'s WOMB TWINS TRIPLETS QUADRUPLETS I WILL SINGLEHANDEDLY FIX EUROPE\'S DECLINING BIRTHRATES WITH MY {waifu}'.format(msg))
  if pesan.content.startswith('$2en'):
        channel = pesan.channel
        await channel.send('write the name first')

        def check(m):
            waifu = m.content
            return m.content == waifu and m.channel == channel

        msg = await client.wait_for('message', check=check)
        waifu = msg.content.upper()
        await channel.send(f'God Damnit I wanna breed {waifu} so bad I can\'t even function normally, there is nothing more I crave on God\'s green earth than to pump their womb full of my hot, goopy semen. I will not die happy until I empty every last nut I have inside of these gorgeous girls. The cute voices, the curvaceous Bodies, the pop-up headlights, I have never been more erect in my life. My parents are trying to convince me to go to therapy because they\'re constantly walking in on me furiously beating my meat red raw to a scene of the hottest twins on Earth, I think they\'re considering taking away my DVD player to convince me to get a girlfriend or something, please help me. I don\'t know if I can live if I lose them, it would be the end of me'.format(msg))

  if pesan.content.startswith('$9id'):
        channel = pesan.channel
        await channel.send('tulis namanya dulu coek')

        def check(m):
            waifu = m.content
            return m.content == waifu and m.channel == channel

        msg = await client.wait_for('message', check=check)
        waifu = msg.content.upper()
        await channel.send(f'Huhahuha Lagi suapin {waifu} eskrim:heart_eyes::heart_eyes:Mana makannya banyak lgi,gpp deh buat {waifu}:heart_eyes::heart_eyes:Cuman gw yg bisa liat,soalnya gw pasangannya:heart_eyes::heart_eyes::heart_eyes::heart_eyes::heart::heart::heart:'.format(msg))

  if pesan.content.startswith('$8id'):
        channel = pesan.channel
        await channel.send('tulis namanya dulu coek')

        def check(m):
          waifu = m.content 
          return m.content == waifu and m.channel == channel
        
        msg = await client.wait_for('message', check=check)
        waifu = msg.content.upper()
        await channel.send(f'KESEKSIAN {waifu} TIADA TARA, TIAP HARI GW NGEBAYANGIN {waifu} DIDEPAN GW DAN DIPANGKUAN GUE, TIAP HARI GW NGEBAYANGIN {waifu} JADI MILIKI GW, NGEBAYANGIN KALO LU LAGI MASAK DAN TIBA2 GW MASUKIN DARI BELAKANG. {waifu} GW UDAH GATAHAN NGELIAT WAJAH LO YG IMUT DAN SIAP DI CROT DIMUKA PLEASE SEKALI LAGI GW MINTA SAMA LU LIATIN KETEK LU YG BERKERINGAT,GW UDAH GASABAR NGEJILAT SELURUH TUBUH LU TERUTAMA KETEK SAMPAI MULUT GW KERING, PLEASE {waifu} gausah dengerin org yg ngejelekkin kamu, yakin banyak org yg lebih apresiasi kamu dari segala aspek kamu cantik u\'re worth it and gorgeous :heartpulse: don\'t let them get you down!! semangatt okay :sparkles::heartpulse::heartpulse: i hope u get betterr luv! xx <33'.format(msg))
  if pesan.content.startswith('$10id'):
        channel = pesan.channel
        await channel.send('tulis namanya dulu coek')

        def check(m):
          waifu = m.content 
          return m.content == waifu and m.channel == channel
        
        msg = await client.wait_for('message', check=check)
        waifu = msg.content
        await channel.send(f':kissing_heart::ok_hand::smiling_face_with_3_hearts::heart_eyes::heart_eyes:rela ditindih semaleman sama {waifu} tanpa pegel linux:heart_eyes::heart_eyes::kissing_heart::smiling_face_with_3_hearts::smiling_face_with_3_hearts:,Rela menghekel nasa demi mendapatkan foto ecci desunya {waifu},menggeser venus mo nandomo demi mendapatkan ai no pujaan hati:smiling_face_with_3_hearts::smiling_face_with_3_hearts::smiling_face_with_3_hearts::kissing_heart:'.format(msg))
  await client.process_commands(pesan)

keep_alive()
client.run(os.getenv('kunci'))
