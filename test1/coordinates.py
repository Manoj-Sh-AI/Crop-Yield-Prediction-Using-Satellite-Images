import ee

roi2 = """color: #98ff00"""ee.Geometry.Point([73.9673408017427, 15.398851565602843]),
water = """color: #0b4a8b"""ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([73.57312156336025, 15.518124734283656]),
            {
              "landcover": 0,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([73.38498069421962, 15.519447958924276]),
            {
              "landcover": 0,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([73.493470684454, 15.39767585424914]),
            {
              "landcover": 0,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([73.56859651468676, 15.23012585404999]),
            {
              "landcover": 0,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([73.24999299906176, 15.235426023216533]),
            {
              "landcover": 0,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([73.15798250101489, 15.457912031156452]),
            {
              "landcover": 0,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([72.69488048477137, 15.607315850398304]),
            {
              "landcover": 0,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([72.663294791412, 15.769937736033523]),
            {
              "landcover": 0,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([72.9862992971739, 16.092246256026705]),
            {
              "landcover": 0,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([73.1510942190489, 16.267659432456494]),
            {
              "landcover": 0,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([72.40265061553328, 15.995900833932042]),
            {
              "landcover": 0,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([72.56744553740828, 16.220194565732907]),
            {
              "landcover": 0,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([72.75695969756453, 15.932525082946741]),
            {
              "landcover": 0,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([73.14655228838285, 15.799772737717152]),
            {
              "landcover": 0,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([73.51596757158597, 15.668911308555417]),
            {
              "landcover": 0,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82433981529493, 15.429212782092806]),
            {
              "landcover": 0,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([73.74743551841993, 15.440795686523117]),
            {
              "landcover": 0,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78619460192931, 15.474983971351207]),
            {
              "landcover": 0,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80576399890197, 15.488218599563659]),
            {
              "landcover": 0,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([73.76044539538634, 15.491527124289014]),
            {
              "landcover": 0,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([73.74602583972228, 15.537840905906917]),
            {
              "landcover": 0,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85120815213565, 15.505726292616155]),
            {
              "landcover": 0,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8920635598505, 15.50208716257017]),
            {
              "landcover": 0,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88863033231144, 15.528221308930522]),
            {
              "landcover": 0,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([73.93463558133487, 15.539137123904192]),
            {
              "landcover": 0,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([73.97212973771389, 15.524913372106043]),
            {
              "landcover": 0,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9577960127383, 15.54318905959053]),
            {
              "landcover": 0,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([73.97822894641513, 15.522037898998567]),
            {
              "landcover": 0,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99754085132236, 15.510790360275571]),
            {
              "landcover": 0,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([74.004321475712, 15.499955754576844]),
            {
              "landcover": 0,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([74.02216583748691, 15.489057251629102]),
            {
              "landcover": 0,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01558731595435, 15.497874195296788]),
            {
              "landcover": 0,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([74.02413179112227, 15.480425699146622]),
            {
              "landcover": 0,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0273075265959, 15.472981044525003]),
            {
              "landcover": 0,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([74.03697080838583, 15.458267909517495]),
            {
              "landcover": 0,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0407473586788, 15.453304305072347]),
            {
              "landcover": 0,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Point([74.04675550687216, 15.445858675522933]),
            {
              "landcover": 0,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0506178878536, 15.444369517526757]),
            {
              "landcover": 0,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Point([74.06651749498849, 15.459260616138382]),
            {
              "landcover": 0,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0781904686213, 15.465134032972237]),
            {
              "landcover": 0,
              "system:index": "39"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07904877550607, 15.467450264237836]),
            {
              "landcover": 0,
              "system:index": "40"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0767313469172, 15.465051309947894]),
            {
              "landcover": 0,
              "system:index": "41"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07750382311349, 15.465051309947894]),
            {
              "landcover": 0,
              "system:index": "42"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0460112523524, 15.43534316574204]),
            {
              "landcover": 0,
              "system:index": "43"
            }),
        ee.Feature(
            ee.Geometry.Point([74.04811410422008, 15.434040087028146]),
            {
              "landcover": 0,
              "system:index": "44"
            }),
        ee.Feature(
            ee.Geometry.Point([74.05234126562755, 15.436005043859886]),
            {
              "landcover": 0,
              "system:index": "45"
            }),
        ee.Feature(
            ee.Geometry.Point([74.05108967476599, 15.429651613097208]),
            {
              "landcover": 0,
              "system:index": "46"
            }),
        ee.Feature(
            ee.Geometry.Point([74.05145445519202, 15.424650140110339]),
            {
              "landcover": 0,
              "system:index": "47"
            }),
        ee.Feature(
            ee.Geometry.Point([74.04845038109534, 15.420942039797254]),
            {
              "landcover": 0,
              "system:index": "48"
            }),
        ee.Feature(
            ee.Geometry.Point([74.05048885994665, 15.418708030617408]),
            {
              "landcover": 0,
              "system:index": "49"
            }),
        ee.Feature(
            ee.Geometry.Point([74.05160600703493, 15.413589038590867]),
            {
              "landcover": 0,
              "system:index": "50"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0534535455538, 15.413331635651941]),
            {
              "landcover": 0,
              "system:index": "51"
            }),
        ee.Feature(
            ee.Geometry.Point([74.05650315469416, 15.406726729192924]),
            {
              "landcover": 0,
              "system:index": "52"
            }),
        ee.Feature(
            ee.Geometry.Point([74.05486782655362, 15.40960063483003]),
            {
              "landcover": 0,
              "system:index": "53"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0582595708795, 15.409435144460348]),
            {
              "landcover": 0,
              "system:index": "54"
            }),
        ee.Feature(
            ee.Geometry.Point([74.05924662379698, 15.409290340278792]),
            {
              "landcover": 0,
              "system:index": "55"
            }),
        ee.Feature(
            ee.Geometry.Point([74.06158551005797, 15.409311026596606]),
            {
              "landcover": 0,
              "system:index": "56"
            }),
        ee.Feature(
            ee.Geometry.Point([74.06498845472504, 15.412496694971775]),
            {
              "landcover": 0,
              "system:index": "57"
            }),
        ee.Feature(
            ee.Geometry.Point([74.06717713728119, 15.412041602478936]),
            {
              "landcover": 0,
              "system:index": "58"
            }),
        ee.Feature(
            ee.Geometry.Point([74.06996505744803, 15.413405687558685]),
            {
              "landcover": 0,
              "system:index": "59"
            }),
        ee.Feature(
            ee.Geometry.Point([74.072840385512, 15.41175080822778]),
            {
              "landcover": 0,
              "system:index": "60"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07323786439599, 15.407415045330453]),
            {
              "landcover": 0,
              "system:index": "61"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07205769242944, 15.404911963103205]),
            {
              "landcover": 0,
              "system:index": "62"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07404930177631, 15.40270295834837]),
            {
              "landcover": 0,
              "system:index": "63"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07516510072651, 15.401213490869885]),
            {
              "landcover": 0,
              "system:index": "64"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07581658626975, 15.396864493380646]),
            {
              "landcover": 0,
              "system:index": "65"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07526607812542, 15.39343291694953]),
            {
              "landcover": 0,
              "system:index": "66"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07550670494709, 15.392992333708372]),
            {
              "landcover": 0,
              "system:index": "67"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07628088675824, 15.39222884091725]),
            {
              "landcover": 0,
              "system:index": "68"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0771862806015, 15.392218496909127]),
            {
              "landcover": 0,
              "system:index": "69"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0777880250821, 15.39227568740482]),
            {
              "landcover": 0,
              "system:index": "70"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0783323897017, 15.392848117183734]),
            {
              "landcover": 0,
              "system:index": "71"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07848052367751, 15.393288192132443]),
            {
              "landcover": 0,
              "system:index": "72"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07902865620918, 15.3939992540797]),
            {
              "landcover": 0,
              "system:index": "73"
            }),
        ee.Feature(
            ee.Geometry.Point([74.07927810164756, 15.39476093711764]),
            {
              "landcover": 0,
              "system:index": "74"
            }),
        ee.Feature(
            ee.Geometry.Point([74.08004207291674, 15.396195713549861]),
            {
              "landcover": 0,
              "system:index": "75"
            }),
        ee.Feature(
            ee.Geometry.Point([74.08059268668626, 15.396688520963934]),
            {
              "landcover": 0,
              "system:index": "76"
            }),
        ee.Feature(
            ee.Geometry.Point([74.08125954505806, 15.394852288771945]),
            {
              "landcover": 0,
              "system:index": "77"
            }),
        ee.Feature(
            ee.Geometry.Point([74.08117557095329, 15.394200898820593]),
            {
              "landcover": 0,
              "system:index": "78"
            }),
        ee.Feature(
            ee.Geometry.Point([74.08182285868747, 15.393638559834777]),
            {
              "landcover": 0,
              "system:index": "79"
            }),
        ee.Feature(
            ee.Geometry.Point([74.08414034183238, 15.390908043758936]),
            {
              "landcover": 0,
              "system:index": "80"
            }),
        ee.Feature(
            ee.Geometry.Point([74.08834604556773, 15.39248033699475]),
            {
              "landcover": 0,
              "system:index": "81"
            }),
        ee.Feature(
            ee.Geometry.Point([74.08948184404983, 15.38551156254311]),
            {
              "landcover": 0,
              "system:index": "82"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0907907620491, 15.381353095672399]),
            {
              "landcover": 0,
              "system:index": "83"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0916919842781, 15.38393921667367]),
            {
              "landcover": 0,
              "system:index": "84"
            }),
        ee.Feature(
            ee.Geometry.Point([74.09521989489258, 15.37914167001982]),
            {
              "landcover": 0,
              "system:index": "85"
            }),
        ee.Feature(
            ee.Geometry.Point([74.09366098886005, 15.374328063986475]),
            {
              "landcover": 0,
              "system:index": "86"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84850620643476, 15.414785478765802]),
            {
              "landcover": 0,
              "system:index": "87"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8754570426164, 15.412468659394808]),
            {
              "landcover": 0,
              "system:index": "88"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89571308509687, 15.412965122862909]),
            {
              "landcover": 0,
              "system:index": "89"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91665577308515, 15.40965534400904]),
            {
              "landcover": 0,
              "system:index": "90"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92901539222578, 15.433484574887515]),
            {
              "landcover": 0,
              "system:index": "91"
            }),
        ee.Feature(
            ee.Geometry.Point([73.95047306434492, 15.401215169425582]),
            {
              "landcover": 0,
              "system:index": "92"
            }),
        ee.Feature(
            ee.Geometry.Point([73.96384085098475, 15.36885956169951]),
            {
              "landcover": 0,
              "system:index": "93"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98115798083836, 15.36336210189021]),
            {
              "landcover": 0,
              "system:index": "94"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9950704076274, 15.35422330015334]),
            {
              "landcover": 0,
              "system:index": "95"
            }),
        ee.Feature(
            ee.Geometry.Point([74.00579721648944, 15.340189885728408]),
            {
              "landcover": 0,
              "system:index": "96"
            }),
        ee.Feature(
            ee.Geometry.Point([74.00662521292281, 15.329879508691612]),
            {
              "landcover": 0,
              "system:index": "97"
            }),
        ee.Feature(
            ee.Geometry.Point([74.00916668854552, 15.317775985511961]),
            {
              "landcover": 0,
              "system:index": "98"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01066872559386, 15.311650057673532]),
            {
              "landcover": 0,
              "system:index": "99"
            }),
        ee.Feature(
            ee.Geometry.Point([74.03146006482086, 15.303620952775248]),
            {
              "landcover": 0,
              "system:index": "100"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7855706980713, 15.274481196241648]),
            {
              "landcover": 0,
              "system:index": "101"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84187562971192, 15.26371708835499]),
            {
              "landcover": 0,
              "system:index": "102"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8569818308838, 15.289218848174613]),
            {
              "landcover": 0,
              "system:index": "103"
            })]),
    vegetation = """color: #ffc82d"""ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([73.90830850995962, 15.356450064735439]),
            {
              "landcover": 1,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90272951520865, 15.352891084642263]),
            {
              "landcover": 1,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90757023061542, 15.35366896883862]),
            {
              "landcover": 1,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90688358510761, 15.348123480955154]),
            {
              "landcover": 1,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90370784963397, 15.349447789960818]),
            {
              "landcover": 1,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91546665395526, 15.353503434020535]),
            {
              "landcover": 1,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91306339467792, 15.349447789960818]),
            {
              "landcover": 1,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91847072805194, 15.350606553448387]),
            {
              "landcover": 1,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91889988149433, 15.346302542354438]),
            {
              "landcover": 1,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92104564870624, 15.342577845750073]),
            {
              "landcover": 1,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92130314077167, 15.345226525715795]),
            {
              "landcover": 1,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91683994497089, 15.340177450512595]),
            {
              "landcover": 1,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91709743703632, 15.33744593271958]),
            {
              "landcover": 1,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9171832677248, 15.334714379209814]),
            {
              "landcover": 1,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91083179677753, 15.337942574975095]),
            {
              "landcover": 1,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92450472526468, 15.337677314221246]),
            {
              "landcover": 1,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92450472526468, 15.341650414801107]),
            {
              "landcover": 1,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92364641837992, 15.333041934704287]),
            {
              "landcover": 1,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91832491569437, 15.329730886378035]),
            {
              "landcover": 1,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91317507438578, 15.329648109497779]),
            {
              "landcover": 1,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91854916446334, 15.32341573162688]),
            {
              "landcover": 1,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92429982059127, 15.324905754877092]),
            {
              "landcover": 1,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92515812747604, 15.320187311494712]),
            {
              "landcover": 1,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92610226504928, 15.316462149418037]),
            {
              "landcover": 1,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92653141849166, 15.311991867367196]),
            {
              "landcover": 1,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92902050845748, 15.31008782934518]),
            {
              "landcover": 1,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89723410477552, 15.356137776652094]),
            {
              "landcover": 1,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01676677977593, 15.298515287417512]),
            {
              "landcover": 1,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01886963164361, 15.298432498186981]),
            {
              "landcover": 1,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01642345702203, 15.297935762116667]),
            {
              "landcover": 1,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0106728008941, 15.298846444012387]),
            {
              "landcover": 1,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([74.00702499663385, 15.298184130299065]),
            {
              "landcover": 1,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([74.00805496489556, 15.298763654912756]),
            {
              "landcover": 1,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0077545574859, 15.296859496589914]),
            {
              "landcover": 1,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([74.00835537230523, 15.295948806056]),
            {
              "landcover": 1,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01088737761529, 15.296983681355975]),
            {
              "landcover": 1,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01071571623834, 15.302075193372433]),
            {
              "landcover": 1,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01135944640191, 15.301123131428358]),
            {
              "landcover": 1,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01579500764342, 15.311802980348162]),
            {
              "landcover": 1,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01648165315123, 15.309981725304391]),
            {
              "landcover": 1,
              "system:index": "39"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01854158967467, 15.309609193911161]),
            {
              "landcover": 1,
              "system:index": "40"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01987750503145, 15.308522650286449]),
            {
              "landcover": 1,
              "system:index": "41"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01335437270723, 15.31117402448746]),
            {
              "landcover": 1,
              "system:index": "42"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01425559493623, 15.310553142000787]),
            {
              "landcover": 1,
              "system:index": "43"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01588637801729, 15.308380038792533]),
            {
              "landcover": 1,
              "system:index": "44"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0153499362143, 15.307158951851251]),
            {
              "landcover": 1,
              "system:index": "45"
            }),
        ee.Feature(
            ee.Geometry.Point([74.01843984099946, 15.30564810560773]),
            {
              "landcover": 1,
              "system:index": "46"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0208431002768, 15.305503229367641]),
            {
              "landcover": 1,
              "system:index": "47"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99075621761904, 15.34928117971174]),
            {
              "landcover": 1,
              "system:index": "48"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99133557476625, 15.350274406744946]),
            {
              "landcover": 1,
              "system:index": "49"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98916834988222, 15.349094949116859]),
            {
              "landcover": 1,
              "system:index": "50"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9922797123395, 15.34870179509313]),
            {
              "landcover": 1,
              "system:index": "51"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99163598217592, 15.347418866286235]),
            {
              "landcover": 1,
              "system:index": "52"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99524087109194, 15.349157026000283]),
            {
              "landcover": 1,
              "system:index": "53"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99270886578188, 15.350295098924544]),
            {
              "landcover": 1,
              "system:index": "54"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99446839489565, 15.34861902573062]),
            {
              "landcover": 1,
              "system:index": "55"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99534815945253, 15.35010886923429]),
            {
              "landcover": 1,
              "system:index": "56"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99768704571352, 15.347812022726247]),
            {
              "landcover": 1,
              "system:index": "57"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99601334728823, 15.34822587081052]),
            {
              "landcover": 1,
              "system:index": "58"
            }),
        ee.Feature(
            ee.Geometry.Point([74.00032633938417, 15.346591166097593]),
            {
              "landcover": 1,
              "system:index": "59"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99936074413881, 15.34628077768082]),
            {
              "landcover": 1,
              "system:index": "60"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99930090686894, 15.345168831110898]),
            {
              "landcover": 1,
              "system:index": "61"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98667463334141, 15.350735089628062]),
            {
              "landcover": 1,
              "system:index": "62"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98540863068638, 15.352762909001934]),
            {
              "landcover": 1,
              "system:index": "63"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98590215714512, 15.352059382063546]),
            {
              "landcover": 1,
              "system:index": "64"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98401388199864, 15.352183534048532]),
            {
              "landcover": 1,
              "system:index": "65"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98457178147373, 15.354025113152378]),
            {
              "landcover": 1,
              "system:index": "66"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98749002488194, 15.353197439161367]),
            {
              "landcover": 1,
              "system:index": "67"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9877904322916, 15.351645541580133]),
            {
              "landcover": 1,
              "system:index": "68"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98087120032574, 15.353591113134316]),
            {
              "landcover": 1,
              "system:index": "69"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9811716077354, 15.355184379638208]),
            {
              "landcover": 1,
              "system:index": "70"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98146018909233, 15.357245074445713]),
            {
              "landcover": 1,
              "system:index": "71"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98171768115776, 15.358155497992938]),
            {
              "landcover": 1,
              "system:index": "72"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98274764941948, 15.35749337217082]),
            {
              "landcover": 1,
              "system:index": "73"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98384199069756, 15.356272572176994]),
            {
              "landcover": 1,
              "system:index": "74"
            }),
        ee.Feature(
            ee.Geometry.Point([73.98300514148491, 15.355134531851013]),
            {
              "landcover": 1,
              "system:index": "75"
            }),
        ee.Feature(
            ee.Geometry.Point([74.0000064795696, 15.355759405701324]),
            {
              "landcover": 1,
              "system:index": "76"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99835423881643, 15.358035473328457]),
            {
              "landcover": 1,
              "system:index": "77"
            }),
        ee.Feature(
            ee.Geometry.Point([73.99530514734704, 15.359714849133917]),
            {
              "landcover": 1,
              "system:index": "78"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91018253942343, 15.525878810391045]),
            {
              "landcover": 1,
              "system:index": "79"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91125542302939, 15.524162805295463]),
            {
              "landcover": 1,
              "system:index": "80"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90782219549033, 15.52348053424273]),
            {
              "landcover": 1,
              "system:index": "81"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90750033040854, 15.52478304974868]),
            {
              "landcover": 1,
              "system:index": "82"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9132939018807, 15.521164930813308]),
            {
              "landcover": 1,
              "system:index": "83"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91196352620932, 15.522777585949317]),
            {
              "landcover": 1,
              "system:index": "84"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91245705266806, 15.520358598518007]),
            {
              "landcover": 1,
              "system:index": "85"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91947872230799, 15.523625258594004]),
            {
              "landcover": 1,
              "system:index": "86"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91767627784998, 15.522798260933302]),
            {
              "landcover": 1,
              "system:index": "87"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9207232672909, 15.523439184409426]),
            {
              "landcover": 1,
              "system:index": "88"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9205086905697, 15.527532777693086]),
            {
              "landcover": 1,
              "system:index": "89"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92164594719202, 15.52844245405484]),
            {
              "landcover": 1,
              "system:index": "90"
            }),
        ee.Feature(
            ee.Geometry.Point([73.92357713768274, 15.52575476230866]),
            {
              "landcover": 1,
              "system:index": "91"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91244060585291, 15.526829843210535]),
            {
              "landcover": 1,
              "system:index": "92"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91334182808191, 15.524927773186056]),
            {
              "landcover": 1,
              "system:index": "93"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9131221263574, 15.533842340344238]),
            {
              "landcover": 1,
              "system:index": "94"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91140551258786, 15.536695315441865]),
            {
              "landcover": 1,
              "system:index": "95"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91022534062131, 15.53706743971697]),
            {
              "landcover": 1,
              "system:index": "96"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91148532616364, 15.53785128431813]),
            {
              "landcover": 1,
              "system:index": "97"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91365255104768, 15.536982996600209]),
            {
              "landcover": 1,
              "system:index": "98"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91431773888337, 15.537871957790626]),
            {
              "landcover": 1,
              "system:index": "99"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91242946373688, 15.539505155564393]),
            {
              "landcover": 1,
              "system:index": "100"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91423190819489, 15.539939294566908]),
            {
              "landcover": 1,
              "system:index": "101"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91242946373688, 15.54117968667652]),
            {
              "landcover": 1,
              "system:index": "102"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9149185537027, 15.543495065300226]),
            {
              "landcover": 1,
              "system:index": "103"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91665662514436, 15.541717187604887]),
            {
              "landcover": 1,
              "system:index": "104"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91667808281647, 15.543350354898635]),
            {
              "landcover": 1,
              "system:index": "105"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90016799928594, 15.55988802821848]),
            {
              "landcover": 1,
              "system:index": "106"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89853721620489, 15.558606406029034]),
            {
              "landcover": 1,
              "system:index": "107"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90244251253057, 15.559102518791212]),
            {
              "landcover": 1,
              "system:index": "108"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90119796754766, 15.55653925664621]),
            {
              "landcover": 1,
              "system:index": "109"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90261417390752, 15.553810587670073]),
            {
              "landcover": 1,
              "system:index": "110"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90162712099004, 15.552487583630931]),
            {
              "landcover": 1,
              "system:index": "111"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90557533265996, 15.550544406034165]),
            {
              "landcover": 1,
              "system:index": "112"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90368705751348, 15.549676171818467]),
            {
              "landcover": 1,
              "system:index": "113"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89424568178106, 15.553479837457404]),
            {
              "landcover": 1,
              "system:index": "114"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91832382137432, 15.553528955243296]),
            {
              "landcover": 1,
              "system:index": "115"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91306669170513, 15.555740836655874]),
            {
              "landcover": 1,
              "system:index": "116"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90425940264504, 15.568024025397172]),
            {
              "landcover": 1,
              "system:index": "117"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90299339999001, 15.569512291959185]),
            {
              "landcover": 1,
              "system:index": "118"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90247841585915, 15.571393280120622]),
            {
              "landcover": 1,
              "system:index": "119"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90252133120339, 15.573026211933353]),
            {
              "landcover": 1,
              "system:index": "120"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90050431002419, 15.57011172961491]),
            {
              "landcover": 1,
              "system:index": "121"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89964600313942, 15.569036874644882]),
            {
              "landcover": 1,
              "system:index": "122"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89975329150002, 15.567837991319605]),
            {
              "landcover": 1,
              "system:index": "123"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89868040789406, 15.56746592265964]),
            {
              "landcover": 1,
              "system:index": "124"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90144844759743, 15.566246359555105]),
            {
              "landcover": 1,
              "system:index": "125"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89728565920632, 15.569119555995893]),
            {
              "landcover": 1,
              "system:index": "126"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89820833910744, 15.570463123290319]),
            {
              "landcover": 1,
              "system:index": "127"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89601965655129, 15.569574302832194]),
            {
              "landcover": 1,
              "system:index": "128"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8919737025393, 15.574652294458623]),
            {
              "landcover": 1,
              "system:index": "129"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89459153853784, 15.575272386844155]),
            {
              "landcover": 1,
              "system:index": "130"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89326116286645, 15.576243861153783]),
            {
              "landcover": 1,
              "system:index": "131"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8966729327334, 15.577566712404929]),
            {
              "landcover": 1,
              "system:index": "132"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90021344863305, 15.577236000390352]),
            {
              "landcover": 1,
              "system:index": "133"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89791330087792, 15.579187525030052]),
            {
              "landcover": 1,
              "system:index": "134"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89623960245262, 15.581027086388737]),
            {
              "landcover": 1,
              "system:index": "135"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89737685907494, 15.582887300228473]),
            {
              "landcover": 1,
              "system:index": "136"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90016635645043, 15.581461137791106]),
            {
              "landcover": 1,
              "system:index": "137"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89008125055443, 15.580510357333274]),
            {
              "landcover": 1,
              "system:index": "138"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88986667383324, 15.579600911039565]),
            {
              "landcover": 1,
              "system:index": "139"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90089591730248, 15.582949307066402]),
            {
              "landcover": 1,
              "system:index": "140"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90164693582665, 15.57881547691048]),
            {
              "landcover": 1,
              "system:index": "141"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9129779524676, 15.581233777647071]),
            {
              "landcover": 1,
              "system:index": "142"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91493060063044, 15.579538903191162]),
            {
              "landcover": 1,
              "system:index": "143"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91360022495905, 15.578050709216098]),
            {
              "landcover": 1,
              "system:index": "144"
            }),
        ee.Feature(
            ee.Geometry.Point([73.91872860859553, 15.579166855707749]),
            {
              "landcover": 1,
              "system:index": "145"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88856821612035, 15.591113377249975]),
            {
              "landcover": 1,
              "system:index": "146"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8873880441538, 15.591981436509634]),
            {
              "landcover": 1,
              "system:index": "147"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88764553621922, 15.59082402334789]),
            {
              "landcover": 1,
              "system:index": "148"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89215164736424, 15.593448861674084]),
            {
              "landcover": 1,
              "system:index": "149"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89204435900365, 15.592146780714446]),
            {
              "landcover": 1,
              "system:index": "150"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89369659975682, 15.594275575457587]),
            {
              "landcover": 1,
              "system:index": "151"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89316462274724, 15.598433227784886]),
            {
              "landcover": 1,
              "system:index": "152"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88829373117619, 15.602897334246885]),
            {
              "landcover": 1,
              "system:index": "153"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8877358317011, 15.605935351158431]),
            {
              "landcover": 1,
              "system:index": "154"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88423823114567, 15.60574935141597]),
            {
              "landcover": 1,
              "system:index": "155"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88430260416203, 15.60260799695662]),
            {
              "landcover": 1,
              "system:index": "156"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87546755105359, 15.60767134062159]),
            {
              "landcover": 1,
              "system:index": "157"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87829996377332, 15.607526675394181]),
            {
              "landcover": 1,
              "system:index": "158"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8788364055763, 15.609841306788114]),
            {
              "landcover": 1,
              "system:index": "159"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8806388500343, 15.606948013464155]),
            {
              "landcover": 1,
              "system:index": "160"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87997366219861, 15.605005350759614]),
            {
              "landcover": 1,
              "system:index": "161"
            })]),
    bare = """color: #00ffff"""ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([73.85611273080212, 15.602773332601016]),
            {
              "landcover": 2,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85997511178357, 15.602153323247544]),
            {
              "landcover": 2,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86428810387952, 15.60171931558536]),
            {
              "landcover": 2,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86634804040295, 15.60099596744172]),
            {
              "landcover": 2,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86591888696057, 15.603744676821112]),
            {
              "landcover": 2,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86624075204236, 15.60492268385346]),
            {
              "landcover": 2,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86778570443494, 15.60349667447871]),
            {
              "landcover": 2,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86815048486096, 15.60492268385346]),
            {
              "landcover": 2,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86527384830879, 15.608299062251929]),
            {
              "landcover": 2,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8648446948664, 15.606976408993873]),
            {
              "landcover": 2,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8641580493586, 15.604744412280994]),
            {
              "landcover": 2,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8640594281203, 15.612948947402623]),
            {
              "landcover": 2,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86502502336566, 15.611998312791048]),
            {
              "landcover": 2,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86554000749652, 15.610365690891388]),
            {
              "landcover": 2,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86302945985858, 15.612349634791371]),
            {
              "landcover": 2,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86218019426519, 15.61432247921879]),
            {
              "landcover": 2,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86181541383917, 15.615521091155482]),
            {
              "landcover": 2,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85819397060607, 15.618919091398183]),
            {
              "landcover": 2,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85961017696593, 15.618092476929526]),
            {
              "landcover": 2,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85770044414733, 15.621921267289142]),
            {
              "landcover": 2,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86173448650572, 15.6236157917009]),
            {
              "landcover": 2,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86014661876891, 15.62475235510026]),
            {
              "landcover": 2,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85130605785582, 15.625497797150055]),
            {
              "landcover": 2,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84911737529967, 15.626200394268436]),
            {
              "landcover": 2,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84566269008849, 15.62671700825928]),
            {
              "landcover": 2,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84519062130187, 15.625043174201155]),
            {
              "landcover": 2,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84212217418883, 15.621240833672083]),
            {
              "landcover": 2,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84336671917174, 15.62062088015667]),
            {
              "landcover": 2,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84212217418883, 15.628791258661293]),
            {
              "landcover": 2,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83926830379698, 15.629163216161137]),
            {
              "landcover": 2,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83553466884825, 15.628956573189072]),
            {
              "landcover": 2,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83508405773375, 15.628150663605872]),
            {
              "landcover": 2,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8333459862921, 15.627034783563433]),
            {
              "landcover": 2,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([73.821801758692, 15.623658842247629]),
            {
              "landcover": 2,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82130823223326, 15.622522272782149]),
            {
              "landcover": 2,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81710252849791, 15.62334886938231]),
            {
              "landcover": 2,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81817541210387, 15.622894241664895]),
            {
              "landcover": 2,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81553611843322, 15.624154797856704]),
            {
              "landcover": 2,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8084550866339, 15.62655189970837]),
            {
              "landcover": 2,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80635473392283, 15.62892254143349]),
            {
              "landcover": 2,
              "system:index": "39"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80704137943064, 15.627909987688403]),
            {
              "landcover": 2,
              "system:index": "40"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80759927890574, 15.629769776434767]),
            {
              "landcover": 2,
              "system:index": "41"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80532476566111, 15.630926969797958]),
            {
              "landcover": 2,
              "system:index": "42"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80099031589305, 15.630637672070181]),
            {
              "landcover": 2,
              "system:index": "43"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80146238467967, 15.62966645528079]),
            {
              "landcover": 2,
              "system:index": "44"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79882309100901, 15.629707783748641]),
            {
              "landcover": 2,
              "system:index": "45"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79901621005808, 15.628550583496558]),
            {
              "landcover": 2,
              "system:index": "46"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79931661746775, 15.63299337025347]),
            {
              "landcover": 2,
              "system:index": "47"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79191372058665, 15.631856852583477]),
            {
              "landcover": 2,
              "system:index": "48"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79212829730784, 15.629790440659303]),
            {
              "landcover": 2,
              "system:index": "49"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79332992694651, 15.627971980918685]),
            {
              "landcover": 2,
              "system:index": "50"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79105541370188, 15.62774467231591]),
            {
              "landcover": 2,
              "system:index": "51"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78923291098818, 15.626382163093961]),
            {
              "landcover": 2,
              "system:index": "52"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79056328665956, 15.626216846488415]),
            {
              "landcover": 2,
              "system:index": "53"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78571385276064, 15.629667802951234]),
            {
              "landcover": 2,
              "system:index": "54"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78749483954653, 15.632395463920668]),
            {
              "landcover": 2,
              "system:index": "55"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7836539162372, 15.631010973878153]),
            {
              "landcover": 2,
              "system:index": "56"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78292435538515, 15.628593259867083]),
            {
              "landcover": 2,
              "system:index": "57"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77974861991152, 15.626898776626385]),
            {
              "landcover": 2,
              "system:index": "58"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7762510193561, 15.627146750659156]),
            {
              "landcover": 2,
              "system:index": "59"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78425473105654, 15.625762225135237]),
            {
              "landcover": 2,
              "system:index": "60"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78691432265407, 15.638525308192568]),
            {
              "landcover": 2,
              "system:index": "61"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7985014655984, 15.6395584726804]),
            {
              "landcover": 2,
              "system:index": "62"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79770960973894, 15.642699260694945]),
            {
              "landcover": 2,
              "system:index": "63"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80094971822894, 15.641562796913025]),
            {
              "landcover": 2,
              "system:index": "64"
            }),
        ee.Feature(
            ee.Geometry.Point([73.793446095386, 15.644090843424907]),
            {
              "landcover": 2,
              "system:index": "65"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78934768001125, 15.645454582356185]),
            {
              "landcover": 2,
              "system:index": "66"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78823188106105, 15.643780901490992]),
            {
              "landcover": 2,
              "system:index": "67"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78733065883205, 15.641900577028087]),
            {
              "landcover": 2,
              "system:index": "68"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7878356590893, 15.647830294175597]),
            {
              "landcover": 2,
              "system:index": "69"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77575498968622, 15.642251369497673]),
            {
              "landcover": 2,
              "system:index": "70"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77489668280145, 15.640102409781319]),
            {
              "landcover": 2,
              "system:index": "71"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77705833029722, 15.646383920904436]),
            {
              "landcover": 2,
              "system:index": "72"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77289554190611, 15.649958510535773]),
            {
              "landcover": 2,
              "system:index": "73"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77205869269346, 15.649028709995557]),
            {
              "landcover": 2,
              "system:index": "74"
            }),
        ee.Feature(
            ee.Geometry.Point([73.76834651541685, 15.648966723142594]),
            {
              "landcover": 2,
              "system:index": "75"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7671663434503, 15.649111359103633]),
            {
              "landcover": 2,
              "system:index": "76"
            }),
        ee.Feature(
            ee.Geometry.Point([73.76680156302427, 15.647954268551555]),
            {
              "landcover": 2,
              "system:index": "77"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77238055777525, 15.648491489979047]),
            {
              "landcover": 2,
              "system:index": "78"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77437612128233, 15.648160892344483]),
            {
              "landcover": 2,
              "system:index": "79"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77480527472471, 15.648863411679217]),
            {
              "landcover": 2,
              "system:index": "80"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77278825354551, 15.651301548297868]),
            {
              "landcover": 2,
              "system:index": "81"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77081414771055, 15.652148690657654]),
            {
              "landcover": 2,
              "system:index": "82"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78353929641582, 15.656384349811889]),
            {
              "landcover": 2,
              "system:index": "83"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7896761906419, 15.657995943419316]),
            {
              "landcover": 2,
              "system:index": "84"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78980493667461, 15.654400832546777]),
            {
              "landcover": 2,
              "system:index": "85"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79242277267315, 15.655557886623415]),
            {
              "landcover": 2,
              "system:index": "86"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79345274093487, 15.65386362664254]),
            {
              "landcover": 2,
              "system:index": "87"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79293775680401, 15.652210676546199]),
            {
              "landcover": 2,
              "system:index": "88"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79109239700176, 15.660310004327092]),
            {
              "landcover": 2,
              "system:index": "89"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79328107955791, 15.658822396750995]),
            {
              "landcover": 2,
              "system:index": "90"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79984457249247, 15.681827436958535]),
            {
              "landcover": 2,
              "system:index": "91"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80130369419658, 15.681992708607194]),
            {
              "landcover": 2,
              "system:index": "92"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80430776829326, 15.677447689505005]),
            {
              "landcover": 2,
              "system:index": "93"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80207617039287, 15.677447689505005]),
            {
              "landcover": 2,
              "system:index": "94"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82516462559306, 15.680174713110961]),
            {
              "landcover": 2,
              "system:index": "95"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82396299595439, 15.678852524397255]),
            {
              "landcover": 2,
              "system:index": "96"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8261087631663, 15.675381738278034]),
            {
              "landcover": 2,
              "system:index": "97"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81400663609111, 15.68639444010477]),
            {
              "landcover": 2,
              "system:index": "98"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8147791122874, 15.692757159513762]),
            {
              "landcover": 2,
              "system:index": "99"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81151754612529, 15.69168294808512]),
            {
              "landcover": 2,
              "system:index": "100"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81091673130595, 15.696734738353431]),
            {
              "landcover": 2,
              "system:index": "101"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80190450901591, 15.706154320057856]),
            {
              "landcover": 2,
              "system:index": "102"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80216200108134, 15.708550459972042]),
            {
              "landcover": 2,
              "system:index": "103"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78602583164775, 15.715986576787492]),
            {
              "landcover": 2,
              "system:index": "104"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79400808567607, 15.713094785843419]),
            {
              "landcover": 2,
              "system:index": "105"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79666883701884, 15.708880959817503]),
            {
              "landcover": 2,
              "system:index": "106"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78422338718974, 15.70623694604125]),
            {
              "landcover": 2,
              "system:index": "107"
            }),
        ee.Feature(
            ee.Geometry.Point([73.779588530012, 15.707641582632327]),
            {
              "landcover": 2,
              "system:index": "108"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79031736607158, 15.70557593723588]),
            {
              "landcover": 2,
              "system:index": "109"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77675611729228, 15.716730173535337]),
            {
              "landcover": 2,
              "system:index": "110"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77297956699931, 15.720943837140226]),
            {
              "landcover": 2,
              "system:index": "111"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78233511204326, 15.721770035462677]),
            {
              "landcover": 2,
              "system:index": "112"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77744276280009, 15.723339803035923]),
            {
              "landcover": 2,
              "system:index": "113"
            }),
        ee.Feature(
            ee.Geometry.Point([73.73988676792555, 15.704006032729133]),
            {
              "landcover": 2,
              "system:index": "114"
            }),
        ee.Feature(
            ee.Geometry.Point([73.73302031284743, 15.699709390131314]),
            {
              "landcover": 2,
              "system:index": "115"
            }),
        ee.Feature(
            ee.Geometry.Point([73.73216200596266, 15.694338459524523]),
            {
              "landcover": 2,
              "system:index": "116"
            }),
        ee.Feature(
            ee.Geometry.Point([73.72821379429274, 15.692437942498676]),
            {
              "landcover": 2,
              "system:index": "117"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7408309054988, 15.689050020397113]),
            {
              "landcover": 2,
              "system:index": "118"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7434058261531, 15.68938055185987]),
            {
              "landcover": 2,
              "system:index": "119"
            }),
        ee.Feature(
            ee.Geometry.Point([73.73096037632399, 15.706484823790397]),
            {
              "landcover": 2,
              "system:index": "120"
            }),
        ee.Feature(
            ee.Geometry.Point([73.70081228313074, 15.78610352094063]),
            {
              "landcover": 2,
              "system:index": "121"
            }),
        ee.Feature(
            ee.Geometry.Point([73.69995397624598, 15.794197522141513]),
            {
              "landcover": 2,
              "system:index": "122"
            }),
        ee.Feature(
            ee.Geometry.Point([73.68810934123621, 15.791802392206105]),
            {
              "landcover": 2,
              "system:index": "123"
            }),
        ee.Feature(
            ee.Geometry.Point([73.67420476970301, 15.79452788266874]),
            {
              "landcover": 2,
              "system:index": "124"
            }),
        ee.Feature(
            ee.Geometry.Point([73.67042821941004, 15.784038672958298]),
            {
              "landcover": 2,
              "system:index": "125"
            }),
        ee.Feature(
            ee.Geometry.Point([73.74370656582221, 15.756656454373006]),
            {
              "landcover": 2,
              "system:index": "126"
            }),
        ee.Feature(
            ee.Geometry.Point([73.71349416347846, 15.760125855242844]),
            {
              "landcover": 2,
              "system:index": "127"
            }),
        ee.Feature(
            ee.Geometry.Point([73.76228975212439, 15.68004686534427]),
            {
              "landcover": 2,
              "system:index": "128"
            }),
        ee.Feature(
            ee.Geometry.Point([73.75997232353552, 15.678559401507504]),
            {
              "landcover": 2,
              "system:index": "129"
            }),
        ee.Feature(
            ee.Geometry.Point([73.73902963554724, 15.677650390493529]),
            {
              "landcover": 2,
              "system:index": "130"
            }),
        ee.Feature(
            ee.Geometry.Point([73.72735666191443, 15.675419164480587]),
            {
              "landcover": 2,
              "system:index": "131"
            }),
        ee.Feature(
            ee.Geometry.Point([73.76366304314001, 15.672030959835773]),
            {
              "landcover": 2,
              "system:index": "132"
            }),
        ee.Feature(
            ee.Geometry.Point([73.74546693718298, 15.652857621195196]),
            {
              "landcover": 2,
              "system:index": "133"
            }),
        ee.Feature(
            ee.Geometry.Point([73.75679658806189, 15.661866008656203]),
            {
              "landcover": 2,
              "system:index": "134"
            }),
        ee.Feature(
            ee.Geometry.Point([73.75877069389685, 15.653518800745312]),
            {
              "landcover": 2,
              "system:index": "135"
            }),
        ee.Feature(
            ee.Geometry.Point([73.75190423881872, 15.650626124430412]),
            {
              "landcover": 2,
              "system:index": "136"
            }),
        ee.Feature(
            ee.Geometry.Point([73.75362085258826, 15.647650757535354]),
            {
              "landcover": 2,
              "system:index": "137"
            }),
        ee.Feature(
            ee.Geometry.Point([73.73412981454715, 15.651865847861506]),
            {
              "landcover": 2,
              "system:index": "138"
            }),
        ee.Feature(
            ee.Geometry.Point([73.72820749704226, 15.650956718080199]),
            {
              "landcover": 2,
              "system:index": "139"
            }),
        ee.Feature(
            ee.Geometry.Point([73.73455896798953, 15.64451004552688]),
            {
              "landcover": 2,
              "system:index": "140"
            }),
        ee.Feature(
            ee.Geometry.Point([73.73859301034793, 15.647072208946318]),
            {
              "landcover": 2,
              "system:index": "141"
            }),
        ee.Feature(
            ee.Geometry.Point([73.74511614267215, 15.640212150966827]),
            {
              "landcover": 2,
              "system:index": "142"
            }),
        ee.Feature(
            ee.Geometry.Point([73.74683275644168, 15.641947850021083]),
            {
              "landcover": 2,
              "system:index": "143"
            }),
        ee.Feature(
            ee.Geometry.Point([73.75309839670047, 15.643270277514272]),
            {
              "landcover": 2,
              "system:index": "144"
            }),
        ee.Feature(
            ee.Geometry.Point([73.72717752878054, 15.644923299861672]),
            {
              "landcover": 2,
              "system:index": "145"
            }),
        ee.Feature(
            ee.Geometry.Point([73.73284235422, 15.643022323010298]),
            {
              "landcover": 2,
              "system:index": "146"
            }),
        ee.Feature(
            ee.Geometry.Point([73.75824823800906, 15.645005950628471]),
            {
              "landcover": 2,
              "system:index": "147"
            }),
        ee.Feature(
            ee.Geometry.Point([73.75043764535769, 15.635252929702748]),
            {
              "landcover": 2,
              "system:index": "148"
            }),
        ee.Feature(
            ee.Geometry.Point([73.74854937021121, 15.633847795168608]),
            {
              "landcover": 2,
              "system:index": "149"
            }),
        ee.Feature(
            ee.Geometry.Point([73.76777544442996, 15.60805773193588]),
            {
              "landcover": 2,
              "system:index": "150"
            }),
        ee.Feature(
            ee.Geometry.Point([73.767603783053, 15.605577747162648]),
            {
              "landcover": 2,
              "system:index": "151"
            }),
        ee.Feature(
            ee.Geometry.Point([73.76708879892215, 15.602932397023972]),
            {
              "landcover": 2,
              "system:index": "152"
            }),
        ee.Feature(
            ee.Geometry.Point([73.75927820627078, 15.60971103845901]),
            {
              "landcover": 2,
              "system:index": "153"
            }),
        ee.Feature(
            ee.Geometry.Point([73.75541582528933, 15.608719056144482]),
            {
              "landcover": 2,
              "system:index": "154"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78090753976687, 15.610372357336276]),
            {
              "landcover": 2,
              "system:index": "155"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7808217090784, 15.606569744670079]),
            {
              "landcover": 2,
              "system:index": "156"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78871813241824, 15.607396405594873]),
            {
              "landcover": 2,
              "system:index": "157"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78605738107547, 15.609545708406461]),
            {
              "landcover": 2,
              "system:index": "158"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7973012012659, 15.61533218093132]),
            {
              "landcover": 2,
              "system:index": "159"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79386797372683, 15.614340225810993]),
            {
              "landcover": 2,
              "system:index": "160"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79841700021609, 15.612356301171758]),
            {
              "landcover": 2,
              "system:index": "161"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80777254526004, 15.610124363007218]),
            {
              "landcover": 2,
              "system:index": "162"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80760088388308, 15.603924407323312]),
            {
              "landcover": 2,
              "system:index": "163"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80845919076785, 15.620043902199741]),
            {
              "landcover": 2,
              "system:index": "164"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80296602670535, 15.621531791675066]),
            {
              "landcover": 2,
              "system:index": "165"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79927530710086, 15.621614451884701]),
            {
              "landcover": 2,
              "system:index": "166"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83229326325136, 15.60678681441564]),
            {
              "landcover": 2,
              "system:index": "167"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83014749603944, 15.59711464435091]),
            {
              "landcover": 2,
              "system:index": "168"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83375238495546, 15.59281575577522]),
            {
              "landcover": 2,
              "system:index": "169"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83109163361269, 15.591989036113352]),
            {
              "landcover": 2,
              "system:index": "170"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83521150665956, 15.589839549414252]),
            {
              "landcover": 2,
              "system:index": "171"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82508348541933, 15.5906662777306]),
            {
              "landcover": 2,
              "system:index": "172"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77761911469179, 15.589674203351569]),
            {
              "landcover": 2,
              "system:index": "173"
            }),
        ee.Feature(
            ee.Geometry.Point([73.76834940033632, 15.5843830590585]),
            {
              "landcover": 2,
              "system:index": "174"
            }),
        ee.Feature(
            ee.Geometry.Point([73.76654695587831, 15.578843746358201]),
            {
              "landcover": 2,
              "system:index": "175"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77143930512148, 15.577603581265667]),
            {
              "landcover": 2,
              "system:index": "176"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7716967971869, 15.582150816681382]),
            {
              "landcover": 2,
              "system:index": "177"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77598833161073, 15.579009101138407]),
            {
              "landcover": 2,
              "system:index": "178"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77513002472597, 15.575371265240985]),
            {
              "landcover": 2,
              "system:index": "179"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77633165436464, 15.57123728266161]),
            {
              "landcover": 2,
              "system:index": "180"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77495836334901, 15.567351263248067]),
            {
              "landcover": 2,
              "system:index": "181"
            }),
        ee.Feature(
            ee.Geometry.Point([73.77521585541444, 15.588516777185172]),
            {
              "landcover": 2,
              "system:index": "182"
            }),
        ee.Feature(
            ee.Geometry.Point([73.78431390839296, 15.593973157709186]),
            {
              "landcover": 2,
              "system:index": "183"
            }),
        ee.Feature(
            ee.Geometry.Point([73.7808806808539, 15.591079640640583]),
            {
              "landcover": 2,
              "system:index": "184"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79092287140566, 15.59347712910788]),
            {
              "landcover": 2,
              "system:index": "185"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79315446930605, 15.591741019565676]),
            {
              "landcover": 2,
              "system:index": "186"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84087019158449, 15.558897847251856]),
            {
              "landcover": 2,
              "system:index": "187"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84284429741945, 15.55335784801182]),
            {
              "landcover": 2,
              "system:index": "188"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83838110161867, 15.551042580272046]),
            {
              "landcover": 2,
              "system:index": "189"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84584837151613, 15.554019348297734]),
            {
              "landcover": 2,
              "system:index": "190"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85520391656007, 15.556582641826514]),
            {
              "landcover": 2,
              "system:index": "191"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8594954509839, 15.547569629846102]),
            {
              "landcover": 2,
              "system:index": "192"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85245733452882, 15.545171606083677]),
            {
              "landcover": 2,
              "system:index": "193"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8606112499341, 15.541991847623812]),
            {
              "landcover": 2,
              "system:index": "194"
            }),
        ee.Feature(
            ee.Geometry.Point([73.860954572688, 15.537857194517343]),
            {
              "landcover": 2,
              "system:index": "195"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85280065728273, 15.562068010200251]),
            {
              "landcover": 2,
              "system:index": "196"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84619169427003, 15.559670155326959]),
            {
              "landcover": 2,
              "system:index": "197"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84807996941652, 15.572651311552542]),
            {
              "landcover": 2,
              "system:index": "198"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85005407525148, 15.569013363142998]),
            {
              "landcover": 2,
              "system:index": "199"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85383062554445, 15.57496633611559]),
            {
              "landcover": 2,
              "system:index": "200"
            })]),
    houses = """color: #bf04c2"""ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([73.82410578049075, 15.496720322409429]),
            {
              "landcover": 3,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82638029373538, 15.49622405954522]),
            {
              "landcover": 3,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82144502914798, 15.49308103373193]),
            {
              "landcover": 3,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82062963760745, 15.491509502902364]),
            {
              "landcover": 3,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82590822494876, 15.490971871191572]),
            {
              "landcover": 3,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82590822494876, 15.488614546416363]),
            {
              "landcover": 3,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8285260609473, 15.498539942715048]),
            {
              "landcover": 3,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82500700271976, 15.499573810749858]),
            {
              "landcover": 3,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83019975937259, 15.499367037556759]),
            {
              "landcover": 3,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81213239944827, 15.48522326012334]),
            {
              "landcover": 3,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81045870102298, 15.486422623827421]),
            {
              "landcover": 3,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81208948410404, 15.482121425186099]),
            {
              "landcover": 3,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81277612961185, 15.480508452635885]),
            {
              "landcover": 3,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81217531479251, 15.476331208859111]),
            {
              "landcover": 3,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81372026718509, 15.474966348555128]),
            {
              "landcover": 3,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81247572220218, 15.473849637974787]),
            {
              "landcover": 3,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8230328968848, 15.47719975163831]),
            {
              "landcover": 3,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82140211380374, 15.474842269899304]),
            {
              "landcover": 3,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8235907963599, 15.474511393120126]),
            {
              "landcover": 3,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82123045242679, 15.484106604904865]),
            {
              "landcover": 3,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81453565872562, 15.488200977895007]),
            {
              "landcover": 3,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82603697098148, 15.485099187619026]),
            {
              "landcover": 3,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82479242599857, 15.486753481556157]),
            {
              "landcover": 3,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82998479392188, 15.494621254957812]),
            {
              "landcover": 3,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83140100028174, 15.493835496891775]),
            {
              "landcover": 3,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([73.83097184683936, 15.497805612323289]),
            {
              "landcover": 3,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81067947782208, 15.472335730157969]),
            {
              "landcover": 3,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82183746732403, 15.469605947854195]),
            {
              "landcover": 3,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([73.82226662076641, 15.473038850072557]),
            {
              "landcover": 3,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80771831906964, 15.4590173608217]),
            {
              "landcover": 3,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([73.79973606504132, 15.456494219212615]),
            {
              "landcover": 3,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([73.803641361367, 15.455377409018919]),
            {
              "landcover": 3,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([73.81200985349346, 15.460299601339157]),
            {
              "landcover": 3,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([73.80664543546368, 15.465345761130827]),
            {
              "landcover": 3,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8505947412259, 15.463682649279486]),
            {
              "landcover": 3,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84909270417756, 15.463558563860975]),
            {
              "landcover": 3,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84904978883333, 15.468687365852073]),
            {
              "landcover": 3,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84595988404817, 15.464716691542675]),
            {
              "landcover": 3,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84368537080354, 15.471210358921429]),
            {
              "landcover": 3,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84368537080354, 15.47571858144465]),
            {
              "landcover": 3,
              "system:index": "39"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84317038667268, 15.478572359621115]),
            {
              "landcover": 3,
              "system:index": "40"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84763358247346, 15.478737794830154]),
            {
              "landcover": 3,
              "system:index": "41"
            }),
        ee.Feature(
            ee.Geometry.Point([73.84703276765413, 15.472533883972906]),
            {
              "landcover": 3,
              "system:index": "42"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85209677827424, 15.462979497591576]),
            {
              "landcover": 3,
              "system:index": "43"
            }),
        ee.Feature(
            ee.Geometry.Point([73.85884913724283, 15.463465708520593]),
            {
              "landcover": 3,
              "system:index": "44"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8704479647239, 15.469102103226865]),
            {
              "landcover": 3,
              "system:index": "45"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87092003351052, 15.472204133332967]),
            {
              "landcover": 3,
              "system:index": "46"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86403396697733, 15.454960482448188]),
            {
              "landcover": 3,
              "system:index": "47"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86526834613312, 15.449969945986854]),
            {
              "landcover": 3,
              "system:index": "48"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87999369569945, 15.446982991252085]),
            {
              "landcover": 3,
              "system:index": "49"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86660021225134, 15.439093367837721]),
            {
              "landcover": 3,
              "system:index": "50"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86874597946326, 15.439548401045771]),
            {
              "landcover": 3,
              "system:index": "51"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86981886306921, 15.438927900969146]),
            {
              "landcover": 3,
              "system:index": "52"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8667718736283, 15.436487249328932]),
            {
              "landcover": 3,
              "system:index": "53"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86303823867956, 15.433922465822759]),
            {
              "landcover": 3,
              "system:index": "54"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86200827041785, 15.437521427258032]),
            {
              "landcover": 3,
              "system:index": "55"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86140745559851, 15.434915289004918]),
            {
              "landcover": 3,
              "system:index": "56"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8636390534989, 15.430943967779417]),
            {
              "landcover": 3,
              "system:index": "57"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86544149795691, 15.430985336100493]),
            {
              "landcover": 3,
              "system:index": "58"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89840048233191, 15.43164722811646]),
            {
              "landcover": 3,
              "system:index": "59"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89509600082556, 15.426186555869718]),
            {
              "landcover": 3,
              "system:index": "60"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89260691085974, 15.431068072717919]),
            {
              "landcover": 3,
              "system:index": "61"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8956968156449, 15.43379836259103]),
            {
              "landcover": 3,
              "system:index": "62"
            }),
        ee.Feature(
            ee.Geometry.Point([73.9035503236405, 15.433550155904912]),
            {
              "landcover": 3,
              "system:index": "63"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90157621780554, 15.435535801081699]),
            {
              "landcover": 3,
              "system:index": "64"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90054624954382, 15.428585959850448]),
            {
              "landcover": 3,
              "system:index": "65"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90093248764197, 15.430199336590244]),
            {
              "landcover": 3,
              "system:index": "66"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90071791092078, 15.431854068938584]),
            {
              "landcover": 3,
              "system:index": "67"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90256327072302, 15.429620177151953]),
            {
              "landcover": 3,
              "system:index": "68"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89698427597204, 15.417498826790418]),
            {
              "landcover": 3,
              "system:index": "69"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8952911602687, 15.430187626808497]),
            {
              "landcover": 3,
              "system:index": "70"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89948594560803, 15.436858369079605]),
            {
              "landcover": 3,
              "system:index": "71"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87977825157577, 15.441438252229048]),
            {
              "landcover": 3,
              "system:index": "72"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87977825157577, 15.440776391444409]),
            {
              "landcover": 3,
              "system:index": "73"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8777853769609, 15.442886065332607]),
            {
              "landcover": 3,
              "system:index": "74"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88102548545089, 15.443165285268657]),
            {
              "landcover": 3,
              "system:index": "75"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88087528174606, 15.442906748303725]),
            {
              "landcover": 3,
              "system:index": "76"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8688683908913, 15.439382662169608]),
            {
              "landcover": 3,
              "system:index": "77"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86829976258014, 15.440173797707645]),
            {
              "landcover": 3,
              "system:index": "78"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86909369644854, 15.440168626896943]),
            {
              "landcover": 3,
              "system:index": "79"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87003783402179, 15.439548128675458]),
            {
              "landcover": 3,
              "system:index": "80"
            }),
        ee.Feature(
            ee.Geometry.Point([73.86956576523517, 15.439212024697232]),
            {
              "landcover": 3,
              "system:index": "81"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87263196108597, 15.438486521774841]),
            {
              "landcover": 3,
              "system:index": "82"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87180584070938, 15.43821763725991]),
            {
              "landcover": 3,
              "system:index": "83"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8709797203328, 15.438651988995455]),
            {
              "landcover": 3,
              "system:index": "84"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88067132013896, 15.442133315069263]),
            {
              "landcover": 3,
              "system:index": "85"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88048773337005, 15.440693312167255]),
            {
              "landcover": 3,
              "system:index": "86"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88171350288985, 15.440589896187458]),
            {
              "landcover": 3,
              "system:index": "87"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88366883326171, 15.440127109046333]),
            {
              "landcover": 3,
              "system:index": "88"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88370906639693, 15.440253793897098]),
            {
              "landcover": 3,
              "system:index": "89"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88592725325225, 15.440181402563285]),
            {
              "landcover": 3,
              "system:index": "90"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88613110113738, 15.440103840391876]),
            {
              "landcover": 3,
              "system:index": "91"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88597553301452, 15.440455455336668]),
            {
              "landcover": 3,
              "system:index": "92"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88814007568953, 15.439669491696066]),
            {
              "landcover": 3,
              "system:index": "93"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89079896548344, 15.439697931221824]),
            {
              "landcover": 3,
              "system:index": "94"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89078555443837, 15.43989183697539]),
            {
              "landcover": 3,
              "system:index": "95"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88973157591624, 15.441277611484454]),
            {
              "landcover": 3,
              "system:index": "96"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89153133816524, 15.440393405683842]),
            {
              "landcover": 3,
              "system:index": "97"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89203827566905, 15.440455455336668]),
            {
              "landcover": 3,
              "system:index": "98"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89193098730846, 15.440765703322421]),
            {
              "landcover": 3,
              "system:index": "99"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89383535570903, 15.439493683632062]),
            {
              "landcover": 3,
              "system:index": "100"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89407943672938, 15.439400608714339]),
            {
              "landcover": 3,
              "system:index": "101"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8941169876556, 15.439289435841212]),
            {
              "landcover": 3,
              "system:index": "102"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89648806042476, 15.438730985158667]),
            {
              "landcover": 3,
              "system:index": "103"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89635931439204, 15.438767181081806]),
            {
              "landcover": 3,
              "system:index": "104"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89758240170283, 15.439281679592034]),
            {
              "landcover": 3,
              "system:index": "105"
            }),
        ee.Feature(
            ee.Geometry.Point([73.898513128231, 15.43955056272789]),
            {
              "landcover": 3,
              "system:index": "106"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89904538596988, 15.440044376040824]),
            {
              "landcover": 3,
              "system:index": "107"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90022824014545, 15.44061057938755]),
            {
              "landcover": 3,
              "system:index": "108"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89984200204731, 15.44042701591476]),
            {
              "landcover": 3,
              "system:index": "109"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90044281686664, 15.440346868432036]),
            {
              "landcover": 3,
              "system:index": "110"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90077229753842, 15.441048717016056]),
            {
              "landcover": 3,
              "system:index": "111"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90044775024762, 15.440986667540681]),
            {
              "landcover": 3,
              "system:index": "112"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89985498205533, 15.441082327140796]),
            {
              "landcover": 3,
              "system:index": "113"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90104051843991, 15.44045149004518]),
            {
              "landcover": 3,
              "system:index": "114"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90111293808332, 15.440105045906094]),
            {
              "landcover": 3,
              "system:index": "115"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90165742651334, 15.440058508589594]),
            {
              "landcover": 3,
              "system:index": "116"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90206948133141, 15.43915288720172]),
            {
              "landcover": 3,
              "system:index": "117"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90224114270836, 15.43928474348028]),
            {
              "landcover": 3,
              "system:index": "118"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90226506137901, 15.439834658152408]),
            {
              "landcover": 3,
              "system:index": "119"
            }),
        ee.Feature(
            ee.Geometry.Point([73.90065381574345, 15.441398899296647]),
            {
              "landcover": 3,
              "system:index": "120"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89960238980962, 15.441621242722277]),
            {
              "landcover": 3,
              "system:index": "121"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89516867502266, 15.442664797572068]),
            {
              "landcover": 3,
              "system:index": "122"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89492191179329, 15.442954359288937]),
            {
              "landcover": 3,
              "system:index": "123"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89537788732582, 15.442333869400635]),
            {
              "landcover": 3,
              "system:index": "124"
            }),
        ee.Feature(
            ee.Geometry.Point([73.89315890281796, 15.44272968820394]),
            {
              "landcover": 3,
              "system:index": "125"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8873606935856, 15.444792805969666]),
            {
              "landcover": 3,
              "system:index": "126"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88672769225809, 15.445097876779663]),
            {
              "landcover": 3,
              "system:index": "127"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88652920879099, 15.445128900904686]),
            {
              "landcover": 3,
              "system:index": "128"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88497202431995, 15.444601490147997]),
            {
              "landcover": 3,
              "system:index": "129"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88215034043628, 15.444735928311385]),
            {
              "landcover": 3,
              "system:index": "130"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88236491715747, 15.44467905063752]),
            {
              "landcover": 3,
              "system:index": "131"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88082532918293, 15.445009975066878]),
            {
              "landcover": 3,
              "system:index": "132"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87930183446247, 15.444725586917297]),
            {
              "landcover": 3,
              "system:index": "133"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88266532456714, 15.445676993014839]),
            {
              "landcover": 3,
              "system:index": "134"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88319103753406, 15.445852795837672]),
            {
              "landcover": 3,
              "system:index": "135"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88264386689502, 15.44643190996456]),
            {
              "landcover": 3,
              "system:index": "136"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87777833974201, 15.445335728286254]),
            {
              "landcover": 3,
              "system:index": "137"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87746183907825, 15.446556005638465]),
            {
              "landcover": 3,
              "system:index": "138"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87912472857568, 15.447646992077152]),
            {
              "landcover": 3,
              "system:index": "139"
            }),
        ee.Feature(
            ee.Geometry.Point([73.8801010526571, 15.447409143221742]),
            {
              "landcover": 3,
              "system:index": "140"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88122109841413, 15.448701258140952]),
            {
              "landcover": 3,
              "system:index": "141"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88145176838941, 15.448639210955257]),
            {
              "landcover": 3,
              "system:index": "142"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87997655343122, 15.448634040355616]),
            {
              "landcover": 3,
              "system:index": "143"
            }),
        ee.Feature(
            ee.Geometry.Point([73.88038424920148, 15.448659893352554]),
            {
              "landcover": 3,
              "system:index": "144"
            }),
        ee.Feature(
            ee.Geometry.Point([73.87963859509534, 15.448866717212002]),
            {
              "landcover": 3,
              "system:index": "145"
            })]),
    roi3 = """color: #ffff99"""ee.Geometry.Point([73.75034957163689, 15.44327451644618])