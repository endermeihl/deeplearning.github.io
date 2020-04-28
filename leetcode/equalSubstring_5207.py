class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        mid = maxCost
        count = 0
        max = 0
        i = 0
        while i < len(s):
            mid = mid - abs(ord(s[i]) - ord(t[i]))
            if mid >= 0:
                count += 1
                if count > max: max = count
            else:
                i -= count - 1
                if len(s) - i <= max: return max
                mid = maxCost - abs(ord(s[i]) - ord(t[i]))
                if mid >= 0:
                    count = 1
                else:
                    count = 0
                    mid = maxCost
            i += 1
        return max


# print(Solution.equalSubstring(1, "krpgjbjjznpzdfy", "nxargkbydxmsgby", 14))
# print(Solution.equalSubstring(1,
#                               "ujteygggjwxnfl",
#                               "nstsenrzttikoy",
#                               43))
#
# print(Solution.equalSubstring(1,
#                               "adcd",
#                               "bddd",
#                               1))
print(Solution.equalSubstring(1,
                              "wwgwlmqcvscpdhbwavpppsglgpeptxzxrzaikyyvafuqshkqlpzbmogmwknnlkfutlnmrabpitrugoxfglpejtxcdklnmsxzmjqicogcwvwvqwmevfdgeabxqhtrwpmikubmjtvcjtatilrlwtxmfspciwtmfqqtuuyffinwcttxayudjcbhedobzqutqdhmwdjwysbkixmianjugbpefwaqhbtgayhhsfbjgkzjawgcgwgydhhfzpxahzggvtjqdqytfeqqofrdeyouttoeupvrdzlbkstllzzkqojotehdcylrcqzapesioszgiwxgtvarlvbylpccofikzddcxhbbknvstwwzojpfdrckgstewdkczzvgknjramuavjwcnpddokuancphsygnpvagqfvxpbdaqrcqyfmmqylqbxqzhinxfflqjfrctefqrbwwtpmdxvegispktymkzuduoxzffoqpmmvmuzxxslztsslgpecffsipeldhkihtrepzykcahyoykgfyjoyprdudgygyenjjiqgmtvvpwtyvaucyhaydttljcritluodocrkghepjcmjuthsfxsaayocdxyqsjtqogpxyrzmujtvemcpofygfrexbxzmpcxhmmguqwymipbaunwxjbsaqhkwjnzkowinwtympkoguicfgjxeacstdjmmvlrawtqpmuvkhdcbrxuutzqwgpmaxerevceexbdjnukubwwsnjzoyhsipqepvfultncmojczwirvrtingbarmhsjxaaghnonkdeclnobnllyctaviihenxqqoosdhpxocqqrnwxqjxkmpyilfcfdmuormwitdjjrfpajolguqcetjhhfevmsolfdbvtsjrkulkikocgpoegmontxsjybjigopvzqchppemvbwxehbrxeqxcpupbjpvlenyesbmmucjodxflorfcwoooprmxzztnvybkckihingvdqjesinxiwmbzgtmrscvwxlhdceomdplffwzjmbbsnroirwkzphsnqmvlsikjsfdmgvrldjtnehsititcmvgelhmofpgclfbzsxegosjuidpjibnjxkezdmhexwedegaaezcrmikjdqjddqiflcxxotjyypagwmwwhbjehgrrxldbvistsrvsyterumafhaalgyyblanzofrginddpsbbaejhnagqhjysmkkqdrfqewplurdiqkchtntvpeeugictwzygdhnsvlbsfxdxmhyqxdisbixklnipprwpbdrsimtkyvckivtqucmzqcqtgdjieuauwpqbkdcrfcteumegnjsdlhkqhkwkmvcwqykssmhgxxpmjuufjxjstnojcvpicwimcaiqoprinlwusqtcghvjhrbsdfcbayigrxohnznlubpnrhoarsuceowhxaiaprkvryhauapdprqjrcgivhvpkxmvtskdcfmhqdtqrvbsxuhjdwzwsqxfwebciqgtcmlnijnjyuocgsaiiqoknujzxbnrwoehwklrxtypkdmctyhwhuvupokbkfncqdllznagstxzocelfwpcfzfmitvhcfkjcipbeakpduujbnkpgnzuhhpozoiqkjcngbtajnorengqioavuqikugnmcubdqthkqukcfijkgahtbidffaatkydofcuawjlshmzhkujxmvxanhbzrmekheojyiiproxrwbxpeekomnhoyaztevcgkbkikosvqruinlofyeuonsggbygayunbkzfgytjqpnxzxlzmalcpdmgbahniospvdyzhboahedmkchyzrcmfnjvpadlhdudjatmsrmrddqhchkziiwrunecitsqmxnqbdaeiijpfuqjvzsdaxzxvhpkgrzbbnfvehyjussgljdrtjcmlrsepmbfvsffcghrfonuwugomvjgedsojaudjuyyjjgigkpjdwrroajhgkyjczuiqnokxoyiycagrovvpcmclildgiibmdxmsjmzsjabbnjqsxjgivtnqexmqsvgdadybvvydrfpcbifakpwsiyotpbuylhbfinapeknhplidygbgstdajiyjkvsljaoxoagwvcuafqaggppfsvmbauozpimanoevzwgtcuxifmlonvrclgqemmdhukwfpblvxibhaadrqvkuzutkqzopnvtpsoezltbtidcqpeukwfsdoyusfszcrrsqyqrbkaewifntnndplvpwmhvwrijwcqvffcgbijhoqmbcwbpumsiehwcccbsodbijzwzzmiduqedfnvsquaifhndoslauzvxizolrgllhmnsgtfcwpxncxyslfltwjuptrtpdlkikiqtwflztdhpmfcyrmxpkycuajsmyyblluravmwbfxfzpccsrsgmtwqoiqmpxybqlssdktyyrxjgswivkipbokggcenbdepnwmwshvjsubmyvxzdiogihkxihbmqcihtzkvpbirazroovhdnjfuedohbwiirpigsncxpiykikilokrxepzrpyhvbjcodcvbnclquetijnosfgacqkhmylaakmmcglqtabwwzgapzfnturiwejiqpubfyswuxamydfwetnqynftnusqoamgpmblkjcbggdchztyowrjaftviuehiylmpzzixfyfncglhndujpsvkncniiohdavczaitjhsoseqllolqklbombddguhgwrmqechunnhgmdhwkwthtlzigawvugpygdqnyjutmrpaqkgaznbztwygsstgcunbhjnxfilxvfkcwbbrfwrvqrtvevztvmqorpfbilktrymvhjsiufkzjstcjcrgifjmanbyxizdvgcneuijvjrfqxecwmwtxirkjlnbdbuxvqkpqaysqgxndscppihciezffhmyrogfjawvtsolewwxflldqlvkbuufwvnjgyyykmtcblkicywbccpkavzxncfkuecvxtbvsdrlhukgjcogbbvvxkaphzcioihybjfazkrhtzmtefxmhikeiwegtvdqhdcurwkzwbslxgznwdlolfjavyzmieywgtsllbsusnvzbcpmnloceoxfivkafbskmbzzkxhhstxwabbiojhyqfqbybcfceozuxwuoduegjiauwywrvaoksxatehgjbuwzfunnvjzijbetulfogqvzkaejlytkirtkshagfopojpvjmjtdklolbhjwpajingbvttgjcpmzqthiedpmiayyjtjmcuvwhcqysdhdvedxfxxssniinovrweulftmczcbbdykesbthttnngidjcziywzfalclfetfdneghznmbqiyzywrlerkvjcoexrkalokjcqpdjcscwfohofeloihbmarvkmdivdhtkigczmhqliokagnaoydzhitoxzvkvbdsizwqwnvtzwecrtunmyetwnolncsljcmuwwcczutquedhezetvgjhoixuazpqcvfbifrsxfesuaylrzgigfotnnotonnerwyuytedqlacarsbexmfzrizvtuhmgqozwqvnsxgioqpfzkwibedqhmbsikvqthltnrkpkiglqqxgxguhdwpbpksuomnmkzrnmlrlijcjuytrlaucowvobpkjznklyqcfssvxrtrlfgzykxjnsloewbyajlupzdggmndkfawoksjcioyzvrsqbzygihfxcfyhlhurewoouxllscxrqoeheknzrrglqpljgpytrvsdctmqbfbwjfsdydcpeiwataiwtdrnhetqsgoodojdvagjlqhnltbbtntxnskqqiapcmtbvklfqpvdbomnnzqncxgbtkxkesxsflbhlqoamcpiqmtauklkrxnhioormxrhwxftpnmvuzhxvguseqsjygxcodgazhiexllsfgnggeummmkeyhjqpuikzenzbsiqjxfkkvnhgazbibcygfymbvhupcemmagjryctiohpqpmxoezezsonqjkifzevixcthoxnnbtytlrlnasvkzhgnysrhudlldmcmmqvzflhtlvftzcavqybutxvbsmulkhfqgskgyfiogrixxrjbvwizkemtiiysdmnggsoyuhotdmakcubbwsacotkildebgcmytblgrtkcsluiisuiznxilhgikjbjojixcubfwrjxdmrxqrieuiejlbthimnaabqlaigdvenwlvagolgxlokulomcupdnywsipcsgrgomnnxviahbfxaqgvbsccottlnxgpihvfefaoddjjrboewqejbxcywixppefmyizhzsajfmfstnnfuivmiwqyauezskwjatzcsupetjoborweszeydqfnyihxdgzqbwqghduabtkqggqjjjedweopjgwuwxpesdnqsodrekctevqhmrijzmpfanbqbagnlbsbugdadjhvsgaovgutunxqessedfwvmgjlymclspmdtwfaeoltljabmucoczojqtwinbwqkuxagmcqgauruvxdigreuazzcylgyjrdeqtnlypyapyipohzpellmjohkpsaoyathycsxvtkepwzfvevyuezokdquojtzqwtjreyroabnqrjmgsccovmxhxhwjgwpiwuxzznooclbfiqnlwaphzgdajasyidlqgicocofusxbslkuwywuqtcyxkycphnompyodvaplptittnjesqytcpnsiyyrllhquliytkdajkrhqmbolsuxnbdlohrzircxyujvrkhjmfamifcouiqnxikllneokwwaxgociawtjureubtcwhhtzmrpbzmjmuxujzayardvpitavqgeqtxukosfxpjpuwuffgboygjmujjlmzmxxcvtfdhfpwgakvjifbzdrhlbpfnlmamgblylqshgdbidldbtzaeuyrlcovctnkshknkqkrfhgctsyrnkxlmiyegfotdyzydovzbhqdoxnsbikexvxlpfmqlaqdgouqgpqpyolmdilzksrhculsferfhrakpdtbdssqahhdycgdylxxhgqzytwzexajyhkgexrustfmkgrzuwsiakdontzhpaehjmiphvfnrkyvezqwreyjegzsenvbumxufbtkebhfitgwutwfawwhrhmxmdywnbfxypwfjzzcrvadgyafanugfxoxsckuwqnxhrmujvibmjqfczeigsvsynnwujflambpxjaateynxivffidpziiupmdtmeraibqetuamjwuoxzsomcnaoyaerbzwbjsoqgntugggwaxmizugugcfxyxsepefbsasrdrycvwszzvfoenpjgxatzenapvqbavukibnzpwbbelifmonmfekirksexxpskbnypezcrdczpfozfciqulvkojoyrroeifphiqfxreugkvbhlaffjcljtouuannzsrqxcwybbcnwwequgmfgckehrxguflyopeipccftciwueuosddbynrqkaqubptxzppvcmdndgbuwhqzedpkidiadqtcmbvzshaanbxyypqpzcxybnqwdpfymqijvqhwtvjdylwnvajkwafzoijqluegvqadihjrnreopqyzvmaxxnscmyazyhjqqniaotvfotipflhstycifhhfkdalgkmkauqbgsldzuaxkfsjyiqtbwbogounwngivrpecepjshmwscshpbpdczjcrnmpoykldemecjhieslgyomsvlpxkophxxfkbhqucziqxcqyffanerimayvppngcmqdcihmmtfyxpagnsbbbathgorgqkmkrforidezlfdtuxkgzrxjdmoijhdxdypihrhioclnfvupyerdtdrwbrsujkhtoxpymbykmsfsdbctglmtiugoluizuzbchznroqkqflhgrmprncqskxlojyminzeyhcjyoyvwdxqjbphpgiefnduyqlucqkygsquikgcqwbsxektecbkngkvtbrrdrctnwwalzkkiocdhyxiyvexxcabohudwofmtjdbpeyirexqwcepkqvtirmzkggosmxkedrenwrukctovbwbyvugtghefrxfovfzltcybslourkbptiamhabljyiywysqhzofgzmpklcccognirqeljtwoiflonholczsqsjnqdytasyiwdfmzwqertxfgzofqrpkkysfjxwqhslgjusznwrrzfhoxsugnoqxagjvjkqufqfodtefrwjaesauxyghraxtyezkcwkskmnvuydenclchjtyokjjyhfqziupzitvfmrvutrmtpzsoqjlqgdxecjzcmxjbkyhltqnkzudzsgjarasvkaaggsndbsqpiaujjrcwbiaowfneatjloqnhrrmumvwobqmplkaciroimpwmotmibawfjclimculbidxtzukdicnbgwyqipsavmynhdkhanjtkmueyhdivztpbnddtxjdkdktsqiiuwladdnhzkpxdfqhnvagascyzracxkgazarxkyrtovisgsunkfkhuunalmrqpbzasnqzfncdgnqcuxboavgtofuqonidamzattkqnfrpcikwsajgzrhdyxdbdvxylblzbgqkjqiirudnbrzriisqtfhfevylhrxwsvtrbghtznivjrmioqqguwqbolhhjenwxntluqmpkxpnsjygkurtuwmqtapizmisakdkrpnaklcndqbjounjswqegqiumbfdkaefcfsydggzqgythzihmgyjfnirymoulsyozazzpmgwinupzwknhpidotcvyzkhjswbmdxubpdaswpwmxeggevpmtyodldoqrznqhtwxldzcfmumthxdmisrxczcteevjyxbjyiegpzwizkjmvxnjjipcuvqympztpltcvyldcflzrzpjapvjycaihtpjzwchjpjoufrwtjwshegsmfljeueyfcicjfgjjwazzkzlrejeyiqwqkuddhfxfradldarcgzyrqtytduuhilzkbffyhwlasjjwfmitjwoanyrsydlhwmpfkreieanqluonsxlbrfdzgtqhidlnqcbedevffzktqzgvmsacgdbrniswlzprwzrvjdmsqydnwtcgbpthbpqygqmsrsycupnocmdgaxtbjzxomzrhcpxcyakixdzeborhcuvnyfqscgkjlwknfyeazsituypvzupsfjbuixvehrbhhqlcbwjwmrylrkpjiothjwfciacgvyrlruzmvjqloryzfhnqawrzccgrjygjkaezhmzhjnextvksgmccksprfjzxencwdciutjydmzrkpqpoofvchhgjudxnvxdoifccumqitkrdmtftwgsuewnohfajakgwavgooazmrgdnikvrjsjuqzdsbncuighwahrrtfucrtuptimdnawxcqbxwezrfhzfemowvdskzciriambzrpkxgphalgdphbaioakszmzvmytapbuhycfzyznxroyfdwqnhkpkbmsxdweikbylppagfhgqbfikcyayohmwbgwdndwsknbyaqijazkkjjezawidsgmrtxlfzorjdjipbfxfkeqwhrbpirqozoqrgaimyrjbvigidapeoijedhwwkjxsgtrurkmkokicpzpurqhbygrodynnuteyoanbvvfchzlnhlhjvmpbntpxcqlvpbhskdiemfgaflaccavoahwxokytzururdemfusmxmfsmrotxjpcdsazowdmsynrkmxmhyaagrjqunrcpdhejxvofzevkstrrmocekugxjokocmpyyjuezwxtxdkomdipuzvqeqgzdksgbeobngmltorbeowzzcnnonbiujeclcfbbpjodwzxkbsbkrczddswrwdnjmfgvrnfgalueircrplyvgrxoioekuotrlepoyzalsvfmsraphfmctzynqvduvxfffkssggxxksowlvsbzbreiyxrwgretbxelqlbbisxvcrwzzualxvzimmcpknirhdlnpqqjkrvnkvncwhcjhutybmqantbpkzfochmxufaommmkspdhraqwgkfidpesebymumcxvmpqkuwugkxjtsqkpsnxowmoljjwlbmaxaopdkwajlttvgyyyhtczuvrifrydenkvntlwxvcnosgiepeueuirpmdnfswwyuzkqoabrziudcynqagkshdeyccvzviifgeiuvqnjwinhgebtvthjfdqmdlyfuifvwtprimnuxcvjpbxbyuhykxfvfzzeadqcsqjbugnmwpyvlsehninizpedmryguligimntugdmiubyqitepnktnixyoibuffztqmlhchevzhrhbxjcenbpkgpcrollynzhbygcstwdvbcblooiqtbhkzvvqgrlmgvxgspgkfijduyqqnzgtgbloslwzmpcpbwjphvktlifvpghinkmgsuhqmepsawjfvhzzpppnfijcwemzhtbymcyigyaufzhveqaicispplchxplqrobagyqrsdjwghzpifckstjomzffmbaabbzzaarefvxdusgypvzycymxekddkrzlyxinrtnjucamufqeoxuulxkbdkrchazgvqwqkfvatxafuzpfgiarqtdjrtuqvilrolfxsmctpyekgmsbsyrsxtzhrismphrvevvdircpmovkpnxxyajjcaxpazznbgydmwxqaquojoxhpiqclpfyqmmdruohvhoyfoksbkuqwtexjepocdpnjolxbzxvfvxmozcvnftyujryhrjmoxtxtoarhhqwesrlxuhmoqvmwdrubdptgfvfwzjpqfwoixljefruannjkyovvdfgkuntdaiqkbdkhdezpddapmcrhsqmrairyrqavrqcbjrxelfvxizpdrjsffovrlnykonmfcmzyxpptfclapychwdtmlrmptbivcyiwkbxawwodwjijdmoylxczbahutkfujzbtrjqoyjhdacgmdheziaqjsehasklmdnhqxmtsracrtvhjlejezgazknofywetqpetpoiwhikpshainkuwrrrkrapqnzghxofleauoqdldiutvfqbghssoboczqsbkserassgijsdsgewqmgezsjlpyvsuvualiqbdwuhgarowyqkpgwlyikrdcmmersbiclzfoheklqxwxchejxnukogumhgimovoptxtmypafngcqvzqzocptgivhonwqliyizpbhwyryycrktvbofdytpgtxrgyjbapobwbuhpdvsahczahgnamwytfanfxsuzidsxmpbdiurneyujogktnrirnegwlthwmhddlealsbchbibskaxbbfnevuqvznwjcaqszbokayypfikalnupbineruudwycyyumglkghyojpzjcjefzeiteqqirvcuevnlwlhflblivjgkzibuiezximekbqboctibvrrxwjsdziejrxiisomjzpwgraqrkkxavkgzpmwqzjivkvppdoqrigntbzkxdfbvvrgmeyjzokbdtpnamwfynntvgivufyvmuciomkelyynyhihtksqorbgttylfqzrmyvifesqyuwxmrwhspqmxnsukygayhyrgwdyrzmrjfjahmswtpafjmnneciitjmdrgwnensubzsxltgtprpzvdnaipetsmcrtebbwlchrjumaxsudttdtmvaudosmbjnmlvjyziuijrjzqikdwubgplsnkmtgmapyajteemcjbucarcimixpetngljzkzhelusqwacytutzfboettuftnszyycxjnqavtysfnqeecizyiesezunjjqazqlxqchndmlfsmfezznqpuoozsqoumclsfqwuhbwcqhtyecigegmvlxmzutgwdclegulxsevabmwvvatmutpwhoeuecyfimuktjjtynowuswueluttuwoduskplstuyruwxhbokndgoqffmogncbfazftgbvkbwiwkaqjendxwzttgvzewtiirvvlij",
                              "gptninuorlksygfzadfxclyqtldicnvpfpfaguozbtfvmitgzmvodusoukorwsxtmcysnnphtwhptnbnrsioonbpwsvvlyuzfczaathysbcweicuowprjjmgmrbpmagjqxpkgityqibjspjeiysxpsclofbdntzxzwnsbjexjowupyioudyyayentnzqizilekgadkueyexqdemlivgkmitmxqafebebkirofmdjmjyhtbkthfiqlmiyarnvrqhwhmoejukpdlugsmecyofwwurmxvzeabrmmmtgftpfvdasbkbuwglwjwxzljepgoexqkjcppjritzdupobncyxlopsolqwsupjxhlbzafcytmuricimxfifeqcbkteqzqfkfsdzcbhxhocqtxbmvckjhvumpjzaamxuarnznvuapovomxtzyrllwmorketbeujpfiumcfgcpsxaofdcbueuacldynutjmpckamvqwdvdtpgpndkjocplvzeczibgohvmsrfbveqaymqbogowayzrourvsobcgknmjdmtkshaddxjgnntiomobuuzuxnmxwlmwbjirwqgzzmujiwgndfsnrqeeordbonjotawmrcoqlbsurdblfpiljredjezzflmmvprstycouttwvhmyuzexesiryllgbobugxtxdinqvquonpavtvfrphmvbownjxzluzffnqvtqwaiotbftennftnxuptcvjolprstimmmdchjmeybotcpelbqaotfhthappeggvznoblpoarvltrgyyjvliwqajgfzdafuxclaeszlvtesxslryqulmwtboebrjqyycsqgqscktxvphstdeprbcjqrpekclxmxredlosuatcetmupllcpzgwkihzltveeqchflrmoaotktfxorhijkjqwxqsuwvzilrdxquqdhhvtibqjvgxutnkzpncyotlqsofxevydjtuqayalbnskztlniamrglpfhktnijnjdfbxftiyrdvwokcluvxblwckhtdzetaomkjjvbhzhynzsnyqdzjysbafuwwipwxmytwekcjeloaxmkbssghpivlcgtdnqkvfewwegaqksmijjlwuczgvpiadjwsvbvssxeqejueisddnbqucfyyirlxlypbqnehnqwnmiseazwbhbwxzrheulcebwrewnswgvoaaqurjmjnrpefxnqmwqvrduqyhnkkdehlgwqrmjbpmzjrzejpozliczivbnvqwaqjwdpobgftnrxmifldxkyxrikauwguvhdztsiwvxugaplvfczebxltnpoicgjbqnnrwbluyfdialktegfzmnesivdrvfzntwiymkpcyxvnyjvnxcuotpyxrzlyezkvyrbfanaasaxumsukoozfxipslficywfnfboliecwbewrtbucsjhzwdhzetryrxhatnmkprhgczcxscplfwsfcqwxczmfrhcpjelurtdkityqgtyacyargziolgvslnyyrnrizdmedemhtsdggylepitnsgvjanzzktgutuqwushkdpsuwngzpfazhmzcverxctjcvjotfkghrsririqgwulyitvgajmxyfkyolftddhbypyhqywhlaygwtvvdyuztbndablojysrlrcmhaytcvmlydwihejfnfjewnvjqcejahtebounfpjrpicdueonwmtjlakazvmvgzcjmzbpqnvhebgvucftlkxeokrkecbbqnbycatovyvbnnbqzritgygubzeputbdbfqfyvpbcrgivuizaspjtluyubwkjqukuzfunblvkfrzmakknydrfbxqkfbumewynpmrnslofjdnokafclyreefnixksbffdwqtalezydyxikcglcqqywkmgisihculuzfswqqcxxzvcocqelbyzggpzibbqesrafvcuvyxewemeiorefvalucsfchopsgxwpkqaxuqyptrzgmesjqgxktuvklrwovadygfsvmulayjnmgpdtqfnusvbmofucqiaadgmoxukfsgzwxbkimhdtgvagsgkzogfronndvxyobzklfbdrfwhlorvagetbxenozefgohnhzvsriaaudqztgjlxuhxctvaleeameukgyqaughvpsdqezzkvwhsanjrikgrqikxvpkbdcexgjefqmqowxlfnhomnebqdirakvizgwikdfsxmaerqbwztohpblxkpkyghcipxilnzvhstbpynafmnzpouvelzohsaknaqduodiachbusxxymslmdegnxmpwprobjambgsoxrlafdfficmeoypeingxmgfrgdxuwshdzqyghnhakxgbxktyqtbmcnhmifukvhjoujrthtkamoetibnwrdgtsddyzymnrlqfgieyxmbenvjgexgxcueejwswgilemefbsgooijldglhsisauimdwnklojtplvzrypymphgjmyqatyqdvmhcbjcgwmtaapuantboafdotzjlhhaxdiqxptcvqdyyiawlexqjvtpjpjezrtrywcuqvrklmkdzkjpeyeugkbytbzrzkmoqybdkbdvjuuifnskfebhxgazbdkhuulfjqxqjnvoneetdbksdvtumcmykhztmbbgrrnedetpiaxjiptvucqegnnoldyfuidxnhgaaxmpdzzitkkdwtvjzwxhuvhohbvtipvbchnaocykxoclowhfwpvdjjgpirlhslryzuolxpbxtopjxzzvfqqtprbtrhsqpsvvbrcfjqyrghgzoyycjeehdojxstvudvlqulialxriijjlgdyovcicjccxmaztjylnrhsuqdyfoyfrgxjzwjbwrklzqmpsiqmzkahdcyqjfsyvscxsyoztrqbuwwijthgbvntpdfniobvvbbrfpycpvtmmrlydjabtnzcmcdrvkmevwzlxlfczykeqlxkuckvgvpksklplqdxupnsofcwpyhtsgthgrumjltwjwcnfltdxtpxyqsydogchpdcctotjkfjttjjwmqscixagwuwajydjjwtkuuxguddoszjgonzxsymxeaweuqdhdmpsajbgaixylvosuujlufmknwxfymyxfwwrhguexctbulcchhmbcriysnjkbckvodyvvimfhcwvhqribmbpjqqryhrevauomaqmipsmzdkbkpflgzcjjkyweqtghzoyccryspexmsrtxtfszlpfwkpkgjciiavybloawvlaqjrozfbffofzaxhfuifoahtxbzhtjazboreanurxuimqyaclqzntfbreafogrmsclbzfrvojmlvbvxajvsqbtijuzavgoucdxytzejgvmtuecozhbxqfjnwrwqhcaljjwstftxsbriixjiwgaxnkmcgiggrgjscsftuwtqiipedymmeeqcaozwklxjwqlubqgpdilfuxiqobkxoymixhsrpxecwwnqelrymaekavlmvnlfhmlztiemqtbzsyohowrkkznkionspjsjpgecjsftdghejzxclaacqprkeuuidyzgzyiezvxvqfjiqtpbhrnwkdhdxkwwikcvfnxcqjpygmpbxixiavonbuvxwjtpqnfwatbhyttwpadtgitajqrbqngvfygzuwskwnsiasbaojibzeocnctslsadnyzemxtdqhicnkepcrxclsomtxgegndoezvukokpenvcnpzgppgfeieinxlxcaliwjorsuilvbbtckxrysvqoyyzqqtwgeopmipcvbpxldslvmuccxeyqpmvuauccxvbeoatswysqvjbppfnfoxoatllzolrultjjlotzmjvvgcnswaubvnjeloazouqkzfgrptqunrhkofxeavmwnsazhfhyxxxmptyajmkjmeeykzbuwdrkbpiujglhoiryfttxwrclfvjmzcdcedhyaujdddqydsxasabqixxqmkqfxfreltzkmycdhkrrhhihmakfirhkkpbgviomrcwxqqfmpvcvdufeysovoiuuleldonltfvvidcoypgcqrkosxfyjtvqqnwocswtodkybccwhuwcebgpedqadfxyatgnmbrizwkcgqanntkmsjhtpnrfxxoruxxdhqtxtskmndnjxgftenlqezhtwwjnoowilfmewdxmdercepcetgbkztfbxskazechhebzqegamslzktekxjwccmoijrkkngbktdtypssxfffuaksdztfoxkisazxpjyxhtwjnnyyyyityqcddrtydnhvrrraveztuxpegbowdztxrvsfvbithnqmwipgdjzibxknnjbvwochhlexujnymrwxokkhzqbqjxsbeqedffathzkmfhcqhcwrjpnbztiwqqmwxhmfdrifncljejyqfeavnctpfnvilbmntmvfazahfuhioskedjtruyjijtcodyukhvsttrwdkfxnzyqffuvscylabdmjqjknravncumkfuawsobqlkftlynypijfzyiuizyvemzqiovhxvsvnfejpjrjmisyrrqlfimohonetczeypgipqvqlhamobcmhedozcgztchkwsqkonzaycybzqngnmugwxgksboykfuikbgiubtesbpfmexwrodxmbsjzflqcbmmjwxjxdqmwigsbiisjehszphtpkpwvktiwmpvroeluskbvflzzebwidwdkrwysujaicvhxnfqyjedopxvtdqnfuuzsytakvnnyosorixtustfogljaspgeonmoyhrgfaxaeyuennymcehqavwrpwahnamfhxukmmbwkxnjbjblmdcusnabxbrcpjuylwwqonxdfucetaaypxsqjdoduqjcfvxrvkleaernrlxpqhzteizzwodfnrkvbpjdkarudlqohtfbwbhawiwfmvlsczqqlqrpommufpfbgujcyhlwkfoksciddagofpyqikvxnrxatuugfotlrlzlgakxxpzwizvfhoddsjgmdkpadmzomayddhgsgxaeajerbrcodxtgsyvxgzuhlrgnhvjhzibwzpqrobypvylanaweurbdvrulkvpmgqcavyeddlmhvwjvsnzlvnjskraobxuydirtnjlzfafbfraypqujkiltcjbgimgtajomlegfudvoosftlkqmpuxhvpejfvezewkulginlxfimhsfcyzfuixjkgyyiutyczboyjqhwojzuhpxkfnfwxffvwkluofioujdszztslxqlpnzlgvivdktdxuqjhoaeyprpmiksexdgbzaikrodpakyouyncqzloljxhjpgsvazkrsrsbxozneybtzsaeapcrswoknpwlpkdmvqwvbwkxrpqqelpzrllodsngdijbctaswmhrnhmnclqzllcupteypojpccqgqaettdbawijgltaydqtlpplltjvxspvdasvakvwvpohtublgzxdgsmdzsjwukxtkukzfvzcygglzblypzkokeapgdomupkktsudckeckdmdzrhcaceiohrtqpxmznvaelpmjmvslculyuzqgguahenxmsojwvirfgunamtrrtlaaxusfmcshnsrzuqtsoxexeqoeuxojalexgixiunlyyzpixswghlyftygvwgggoljrxfmqzpilauzfdezdflfffhpjybtvfvqydplwxwavvgltgwiqeygqxrocrnhokxrggiqtfwzvodvhqmfmlvgekpnedsxootesiurqefzgmcqwnocitqrpitmkkjxhxwsqugoawbvvtjucbdfevrlegmckogvpupjxhqzmfvvciglnguwmnizzgklneyzqveeqzqsnfffvafcjvjsqjcokfzromgrlnaiaqhjdevsoyxrfowxvdgwaepuemguvdhorlfxzaxzwskjsapylecznohrxbmwffrbhfsksnnlhqafcegdlvxlslowamjaaycaospfzmopkbknkueytgwzphsnxafmkwdjfndjvlkmehnleowywcrvmhykifzttobihadeicdzmyvvalqnypvgqoniptgbvvdxmwcgjprfisuugrbgngtealwfubbnjeguxyccqznvwajzyrabenqpkwxffnkvjmvvhfyrznzusgbuatpfbukredldtuxjdhxhrauuwglzabsjxrhuvmuanrpctmbcvybcsnvlsobbuobfhysjasdbufmgwfhkggpxpbnlnsrhllbqurftrotxmksvxyietneosgkaqzmcxshwgaczxyzgpkubvwondyeiwzkeyktttccedwjalghjhfctwpvnpsqdvqbnpyjnszmnazvgqphsrkwnafxtgnofbdessyqpiqfpaldrmnigdvmiwumhpunuqzanuclbxhfsmzkkmuwdtiobbpdrfbjmbwevoeybvuduxszaasyvtubolqwomcijpbpsderjgyywfawovvljbknxhlhikvmdnkzkdhrktipsbfaqlywqobyyvedqffawwlazbhcszyvscesyfwpbjoxlxsesezelszmdvuohvmddjvediejdwhmdujelnnhsczashzvgodiwbuezobogegwyzxxngyysaexuwblcdkorcztdybdracdvycgqgktbiyxyxcbgvtmudwebipzesnozaguevepktrknmwneqehdgccmaiscjvxuzznxaeamcokiwtiajjtkbureoxnxhptqnburwsssanxhaejvpmevipeqbcrojisvktgpykleoiepukbsjpfhozdkiaeglvqddrricwdpzgidneuvkuewxnmhoettyieahkgbyrqfpswyobfsxlqqdpnblarranspaatjertzrcwlkzaeqtvvrzouzovbzuwluswirecyfbavfjikillnhcfintbfftfhgsqiimqbvecsnihmbdjiadtgvbpmapgfjnmtfjkcoqnjyamctcqhctpnhzonhbokjmrbdwrkxjbnvssmvyrttcxkftiiueocvizkfyfopklxuzydsphvgsxsuohvhsosohmvtzwagukpaexlfrlpgeuqfsqmqedgfnshuddrolrtlgatpxwskmqeqlsptdbumcyxgkrjgpykmljcuzaqhecidqxlxlvzmmeclrqwnvgttqbwgtvnldwsedlawofyjdrzodmlqortpxdrgoqrugswvlxllsyxbsfxillpdebifvwthszrawhokegeqiqoukcgrmxcxivpisclakxoounomqspenqzjqlycczsarsjpxhlokvuiypxynmawxkrkroazwfmvwrhosstsloviuywnherhebixvayvrxqgcrslczlipkqboiyxrpawmjgynmiwengztihgpksozsvmestxnkeokciezfehlltpwikpddnjckxeufrfkppqelnqnjwyrworzfiberwbcqewpyaiwnbjquztmlgedxexrzkkfguevjkonghtkdladdjgitazxhpwlaxbnhgtbdjwwcgxfbjqgxoutazdyqyufuhrwkepfvbvrmimovzxryiqdcdbjnyzpgefentxhdmmpufybryivoolyhfctmpbinhwbsqfeulqjlhcndcrwydhcwaqgrbeoyxwzcbhgbcuytkcpnyrkcwieuttbdmlaxicoibkwqcjdkriapgnhsyvydpfnxfeeiizfthbwhhofuknsuvrdedusjmwnjraptqbnrepbddrpkcrgvdcqigmlohtvyykrjbttxmyhbpsddkmnqdqhclfmezaktsilorgumsjilqbzpznxemkdqmwloxljukrpvnuvcgxpmfrskpbpyrdpbzqgkjjdboxwngaiteprbwqihnfhzpoxnbewjwktdggdwilehczeaenorzflebrxvznwztwmaywrshaoqgnnxzksngxrtgvkxugqdkqghpxrmdfozjtpzuhzzehiddwsaywkoirxslqvwljdyvmmhekpcgyygrtozcejdsjifpdxtobwqxwjhlymhtuwtmdythnswvcncppzkjnumkaszhclblyoecatfyefmusulxwhbgkftkqvktmeducupshwgfdphtleaopphbqopiqvfhozfvklmzlmlrupxyjleapcfoedhkcwinxnlpstivoqrvdaphwircrtdyldywitafigsxyjhaldyqugdlmrudsvisdstikmzsdldjzbjyhlqemuvjrknaeuzlrrjdgbnhscvnunialtyrhcrgqubmmbwdjgwugmxqbltakdngisesguifjwqanqronjpvawpxpglcnjgcsofqpfhnqlijorcfeaskkbyzffbsefrfjlcmabqjquliqupgsbdxcnbkqxepzskfrntnplcvfwiqagadhobnibnsvqziyiqkxjnasjoxqiaksznwqxxvcdsxenemczlewdnlqbcmrzehxvotjxytlxvgwpiizmjckjkuujcqqbdffopxfzuqbnwbsvctpqnyrrcwjxbbmtccajbacfftlszjyribpzmsyvcemzfycbsutkqjzpbbdquismltkjetwsplplchhtqjzrsetfjuvjeywcnsqbofgkodplaalepwxthrdtwdqegihmznnytyxsjqwtqkcjcyxaeerlbbdlnnlzgdczbkfmcxwzthflqczptislimkwpxwikejalbauermgtziopxgrmufaweapucjihskrdjygxbewrnczvfqobautvcakzaaetjouuppbqdmdjputqeuaystahfmcojnvisiwivndnsotkacijsiazkyqbvpzphkncyywtfgvjfqqkyilqsbsuusuwptbpgtwclocilrwhrkbbfjowsvufkohkeyjpzwypgiuzghvrwtujrgkigyogcfdxqdaiqzzmwrdosqwfltbcnuwkmvgimopbebghqpezmdxakfiktlwwytdyivzgobxzfymduubthepnpzaxhwrssxeesxwbgyyuqmhwfsinlxglrfqqdjxiupkfrehxjekpajnfjgbkuocmkqassbnwcuhklpxdsycffdgtwaevbkloksgrmxjwsjmfruwicgctzslrzssfyhznkgjojsfxsgoligucsmrdovzcxxhotdbolunbdwindkcscsirlcfwassfcbsxsnullhbjindzdortpmadalepemmytnhwjdanfrgpzvxldzjffxnwwaddhgwenkcxzztuzblcvmcwjbxhzadvstesgbmjrnshiecgwynuatpqnwpuickeukvllxeezxkvvkviyrtfysyksjpgqqjdcrrwmyqcgjnewkkdjxfnitynxqlyavpeqykieculohjnygibrodebcnqribsyaexwxyuedidnzpjujuheyipgyjgmgjuxrsdwwpnpvenvoqcukutsqquvinmvmtvyqmjisaikgxctxxjztmccipceubpjzrjzehydewqnmgttourgnlpnfxyfykebhkkxnhmickhwglcgxicqzwtyrertgadopdnxpvtqfewefpblekohkptssrcwcxaswntjooxbusxdkeelfxqylpsqwwyomxanagnddfymkfyufooynqpszqgqkecfojthnzqladtwhotpzxqkxnoqsetgqnxezwjvtmqiebjjvvbxhummfowkwjnfzsmjfyhurprujegfedkcjfsppquawuizqonvewxnjjhjnvxltilbzbwuuritjqhktvxoixhauooolykhzsnhzgqglenkgmyukjmqkskbbkiwzcoezhzvdsqxrrsrkasxbmoeaacmdvnyfbgwxavqnozvjinywwufieeooasfnsrhkbpiftkdaxekqytpiqvmavtznwqsgvyufwnmcxlhzpomddpjukplpdpfbbrdlufrnfuqknoaxizxifblxyecxubtfusjalievamtlbcnqwfabwqceu",
                              15423))