import re

txt = [r"qxfcsmh",r"ffsfyxbyuhqkpwatkjgudo",r"byc\x9dyxuafof\\\xa6uf\\axfozomj\\olh\x6a",r"jtqvz",r"uzezxa\"jgbmojtwyfbfguz",r"vqsremfk\x8fxiknektafj",r"wzntebpxnnt\"vqndz\"i\x47vvjqo\"",r"higvez\"k\"riewqk",r"dlkrbhbrlfrp\\damiauyucwhty",r"d\"",r"qlz",r"ku",r"yy\"\"uoao\"uripabop",r"saduyrntuswlnlkuppdro\\sicxosted",r"tj",r"zzphopswlwdhebwkxeurvizdv",r"xfoheirjoakrpofles\"nfu",r"q\xb7oh\"p\xce\"n",r"qeendp\"ercwgywdjeylxcv",r"dcmem",r"\"i\x13r\"l",r"ikso\xdcbvqnbrjduh\"uqudzki\xderwk",r"wfdsn",r"pwynglklryhtsqbno",r"hcoj\x63iccz\"v\"ttr",r"zf\x23\\hlj\\kkce\\d\\asy\"yyfestwcdxyfj",r"xs",r"m\"tvltapxdvtrxiy",r"bmud",r"k\"a",r"b\"oas",r"\"yexnjjupoqsxyqnquy\"uzfdvetqrc",r"vdw\xe3olxfgujaj",r"qomcxdnd\"\\cfoe\"",r"fpul",r"m\"avamefphkpv",r"vvdnb\\x\\uhnxfw\"dpubfkxfmeuhnxisd",r"hey\\",r"ldaeigghlfey",r"eure\"hoy\xa5iezjp\\tm",r"yygb\"twbj\\r\"\x10gmxuhmp\"",r"weirebp\x39mqonbtmfmd",r"ltuz\\hs\"e",r"ysvmpc",r"g\x8amjtt\"megl\"omsaihifwa",r"yimmm",r"iiyqfalh",r"cwknlaaf",r"q\x37feg\xc6s\"xx",r"uayrgeurgyp\\oi",r"xhug\"pt\"axugllbdiggzhvy",r"kdaarqmsjfx\xc3d",r"\"vkwla",r"d\"",r"tmroz\"bvfinxoe\\mum\"wmm",r"\"n\"bbswxne\\p\\yr\"qhwpdd",r"skzlkietklkqovjhvj\xfe",r"pbg\\pab\"bubqaf\"obzcwxwywbs\\dhtq",r"xxjidvqh\"lx\\wu\"ij",r"daef\x5fe\x5b\\kbeeb\x13qnydtboof",r"ogvazaqy\"j\x73",r"y",r"n\"tibetedldy\\gsamm\"nwu",r"wldkvgdtqulwkad",r"dpmxnj",r"twybw\"cdvf\"mjdajurokbce",r"ru\"\\lasij\"i",r"roc\\vra\\lhrm",r"pbkt\x60booz\"fjlkc",r"j\x4dytvjwrzt",r"\\uiwjkniumxcs",r"cbhm\"nexccior\"v\"j\"nazxilmfp\x47",r"qdxngevzrlgoq",r"\"lrzxftytpobsdfyrtdqpjbpuwmm\x9e",r"mdag\x0asnck\xc2ggj\"slb\"fjy",r"wyqkhjuazdtcgkcxvjkpnjdae",r"aixfk\xc0iom\x21vueob",r"dkiiakyjpkffqlluhaetires",r"ysspv\"lysgkvnmwbbsy",r"gy\"ryexcjjxdm\"xswssgtr",r"s",r"ddxv",r"qwt\"\x27puilb\"pslmbrsxhrz",r"qdg\xc9e\\qwtknlvkol\x54oqvmchn\\",r"lvo",r"b",r"fk\"aa\"\"yenwch\\\\on",r"srig\x63hpwaavs\\\x80qzk\"xa\"\xe6u\\wr",r"yxjxuj\"ghyhhxfj\"\xa6qvatre",r"yoktqxjxkzrklkoeroil",r"\"jfmik\"",r"smgseztzdwldikbqrh\"",r"jftahgctf\"hoqy",r"tcnhicr\"znpgckt\"ble",r"vqktnkodh\"lo\"a\\bkmdjqqnsqr",r"ztnirfzqq",r"s",r"xx",r"iqj\"y\\hqgzflwrdsusasekyrxbp\\ad",r"\\xzjhlaiynkioz\"\"bxepzimvgwt",r"s\x36rbw",r"mniieztwrisvdx",r"atyfxioy\x2b\\",r"irde\x85\x5cvbah\\jekw\"ia",r"bdmftlhkwrprmpat\"prfaocvp",r"w\\k",r"umbpausy",r"zfauhpsangy",r"p\"zqyw",r"wtztypyqvnnxzvlvipnq\"zu",r"deicgwq\\oqvajpbov\\or\"kgplwu",r"mbzlfgpi\\\\zqcidjpzqdzxityxa",r"lfkxvhma",r"\xf2yduqzqr\"\\fak\"p\"n",r"mpajacfuxotonpadvng",r"anb\\telzvcdu\\a\xf2flfq",r"lrs\"ebethwpmuuc\"\x86ygr",r"qmvdbhtumzc\"ci",r"meet",r"yopg\x0fdxdq\"h\\ugsu\xffmolxjv",r"uhy",r"fzgidrtzycsireghazscvmwcfmw\\t",r"cqohkhpgvpru",r"bihyigtnvmevx\"xx",r"xz",r"zofomwotzuxsjk\"q\"mc\"js\"dnmalhxd",r"\\ktnddux\\fqvt\"ibnjntjcbn",r"ia",r"htjadnefwetyp\xd5kbrwfycbyy",r"\"\\hkuxqddnao",r"meqqsz\x83luecpgaem",r"cvks\x87frvxo\"svqivqsdpgwhukmju",r"sgmxiai\\o\"riufxwjfigr\xdf",r"fgywdfecqufccpcdn",r"faghjoq\x28abxnpxj",r"zuppgzcfb\"dctvp\"elup\"zxkopx",r"xqs\x45xxdqcihbwghmzoa",r"anbnlp\\cgcvm\"hc",r"xf\"fgrngwzys",r"nrxsjduedcy\x24",r"\x71sxl\"gj\"sds\"ulcruguz\\t\\ssvjcwhi",r"jhj\"msch",r"qpovolktfwyiuyicbfeeju\x01",r"nkyxmb\"qyqultgt\"nmvzvvnxnb",r"ycsrkbstgzqb\"uv\\cisn",r"s",r"ueptjnn\"\"sh",r"lp\"z\"d\"mxtxiy",r"yzjtvockdnvbubqabjourf\"k\"uoxwle",r"\x82\"wqm\"",r"\xb5cwtuks\x5fpgh",r"wd",r"tbvf",r"ttbmzdgn",r"vfpiyfdejyrlbgcdtwzbnm",r"uc",r"otdcmhpjagqix",r"\\\xb1qso\"s",r"scowax",r"behpstjdh\xccqlgnqjyz\"eesn",r"r\xe1cbnjwzveoomkzlo\\kxlfouhm",r"jgrl",r"kzqs\\r",r"ctscb\x7fthwkdyko\"\x62pkf\"d\xe6knmhurg",r"tc\"kw\x3ftt",r"bxb\x5ccl",r"jyrmfbphsldwpq",r"jylpvysl\"\"juducjg",r"en\\m\"kxpq\"wpb\\\"",r"madouht\"bmdwvnyqvpnawiphgac\"",r"vuxpk\"ltucrw",r"aae\x60arr",r"ttitnne\"kilkrgssnr\xfdurzh",r"oalw",r"pc\"\"gktkdykzbdpkwigucqni\"nxiqx",r"dbrsaj",r"bgzsowyxcbrvhtvekhsh\"qgd",r"kudfemvk\"\"\"hkbrbil\"chkqoa",r"zjzgj\\ekbhyfzufy",r"\\acos\"fqekuxqzxbmkbnn\x1ejzwrm",r"elxahvudn\"txtmomotgw",r"\x2eoxmwdhelpr\"cgi\xf7pzvb",r"eapheklx",r"hfvma\"mietvc\"tszbbm\"czex",r"h\"iiockj\\\xc1et",r"d\"rmjjftm",r"qlvhdcbqtyrhlc\\",r"yy\"rsucjtulm\"coryri\"eqjlbmk",r"tv",r"r\"bfuht\\jjgujp\"",r"kukxvuauamtdosngdjlkauylttaokaj",r"srgost\"\"rbkcqtlccu\x65ohjptstrjkzy",r"yxwxl\\yjilwwxffrjjuazmzjs",r"dxlw\\fkstu\"hjrtiafhyuoh\"sewabne",r"\x88sj\"v",r"rfzprz\xec\"oxqclu\"krzefp\\q",r"cfmhdbjuhrcymgxpylllyvpni",r"ucrmjvmimmcq\x88\xd9\"lz",r"lujtt\"",r"gvbqoixn\"pmledpjmo\"flydnwkfxllf",r"dvxqlbshhmelsk\x8big\"l",r"mx\x54lma\x8bbguxejg",r"\x66jdati\xeceieo",r"\"iyyupixei\x54ff",r"xohzf\"rbxsoksxamiu",r"vlhthspeshzbppa\x4drhqnohjop\"\"mfjd",r"f\"tvxxla\"vurian\"\"idjq\x3aptm\xc3olep",r"gzqz",r"kbq\\wogye\\altvi\\hbvmodny",r"j\xd8",r"ofjozdhkblvndl",r"hbitoupimbawimxlxqze",r"ypeleimnme",r"xfwdrzsc\\oxqamawyizvi\\y",r"enoikppx\xa1ixe\"yo\"gumye",r"fb",r"vzf",r"zxidr",r"cu\x31beirsywtskq",r"lxpjbvqzztafwezd",r"\\jyxeuo\x18bv",r"b\"vawc\"p\\\\giern\"b",r"odizunx\"\"t\\yicdn\"x\"sdiz",r"\"\"tebrtsi",r"ctyzsxv\xa6pegfkwsi\"tgyltaakytccb",r"htxwbofchvmzbppycccliyik\xe5a",r"ggsslefamsklezqkrd",r"rcep\"fnimwvvdx\"l",r"zyrzlqmd\x12egvqs\\llqyie",r"\x07gsqyrr\\rcyhyspsvn",r"butg\"",r"gb",r"gywkoxf\"jsg\\wtopxvumirqxlwz",r"rj\"ir\"wldwveair\x2es\"dhjrdehbqnzl",r"ru\"elktnsbxufk\\ejufjfjlevt\\lrzd",r"\"widsvok",r"oy\"\x81nuesvw",r"ay",r"syticfac\x1cfjsivwlmy\"pumsqlqqzx",r"m",r"rjjkfh\x78cf\x2brgceg\"jmdyas\"\\xlv\xb6p",r"tmuvo\"\x3ffdqdovjmdmkgpstotojkv\"as",r"jd\\ojvynhxllfzzxvbn\"wrpphcvx",r"pz",r"\"twr",r"n\\hdzmxe\"mzjjeadlz",r"fb\"rprxuagvahjnri",r"rfmexmjjgh\\xrnmyvnatrvfruflaqjnd",r"obbbde\"co\"qr\"qpiwjgqahqm\\jjp\"",r"vpbq\"\"y\"czk\\b\x52ed\"lnzepobp",r"syzeajzfarplydipny\"y\"\xe8ad",r"mpyodwb",r"\x47rakphlqqptd",r"wa\"oj\"aiy",r"a",r"ropozx",r"q\x51nbtlwa",r"etukvgx\\jqxlkq",r"\"tp\"rah\"pg\"s\"bpdtes\\tkasdhqd",r"dn\"qqpkikadowssb\xcah\"dzpsf\\ect\"jdh",r"pxunovbbrrn\\vullyn\"bno\"\"\"myfxlp\"",r"qaixyazuryvkmoulhcqaotegfj\\mpzm",r"bvfrbicutzbjwn\\oml\"cf\"d\"ezcpv\"j",r"rmbrdtneudemigdhelmb",r"aq\\aurmbhy",r"wujqvzw",r"gf\"tssmvm\"gm\"hu\x9a\xb7yjawsa",r"hrhqqxow\xe2gsydtdspcfqy\"zw\\ou",r"ianwwf\\yko\\tdujhhqdi",r"xylz\"zpvpab",r"lwuopbeeegp",r"aoop\x49jhhcexdmdtun",r"\\\\mouqqcsgmz",r"tltuvwhveau\x43b\"ymxjlcgiymcynwt",r"gsugerumpyuhtjljbhrdyoj",r"lnjm\xb8wg\"ajh",r"zmspue\"nfttdon\\b\"eww",r"\"w\x67jwaq\x7ernmyvs\\rmdsuwydsd\"th",r"ogtgvtlmcvgllyv",r"z\"fqi\"rvddoehrciyl",r"yustxxtot\"muec\"xvfdbzunzvveq",r"mqslw",r"txqnyvzmibqgjs\xb6xy\x86nfalfyx",r"kzhehlmkholov",r"plpmywcnirrjutjguosh\\",r"pydbnqofv\"dn\\m",r"aegqof",r"eambmxt\\dxagoogl\\zapfwwlmk",r"afbmqitxxqhddlozuxcpjxgh",r"vgts",r"bfdpqtoxzzhmzcilehnflna",r"s\"idpz",r"\xcfhgly\"nlmztwybx\"ecezmsxaqw",r"aackfgndqcqiy",r"\x22unqdlsrvgzfaohoffgxzfpir\"s",r"abh\"ydv\"kbpdhrerl",r"bdzpg",r"ekwgkywtmzp",r"wtoodejqmrrgslhvnk\"pi\"ldnogpth",r"njro\x68qgbx\xe4af\"\\suan"]

l_code_tot = 0
l_str_tot  = 0

hex_pattern = r"\\x[0-9a-f]+"

for l in txt:
    l_str  = len(l)
    l_code = l_str + 2

    hex_str = re.findall(hex_pattern, l)
    n_hex   = len(hex_str)
    
    l_2 = l
    for hs in hex_str:
        l_2 = l_2.replace(hs, "")
    
    n_bs = l_2.count(r'\"')
    n_qs = l_2.count(r"\\")
    
    l_str -= (n_bs + n_qs + (n_hex * 3))
    
    print(l, l_code, l_str)
    
    l_code_tot += l_code
    l_str_tot  += l_str

print(l_code_tot - l_str_tot)

# PART 2
l_code_tot = 0
l_enc_tot  = 0

for l in txt:
    l_code = len(l) + 2
    l_enc  = l_code + 4

    hex_str = re.findall(hex_pattern, l)
    n_hex   = len(hex_str)
    
    l_2 = l
    for hs in hex_str:
        l_2 = l_2.replace(hs, "")
    
    n_bs = l_2.count(r'\"')
    n_qs = l_2.count(r"\\")
    
    l_enc += ((2 * (n_bs + n_qs)) + n_hex)
    
    l_code_tot += l_code
    l_enc_tot  += l_enc

print(l_enc_tot - l_code_tot)