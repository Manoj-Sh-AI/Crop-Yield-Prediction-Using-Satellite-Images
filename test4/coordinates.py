import ee

roi = """color: #d63000"""ee.Geometry.Point([73.94912545952002, 15.370769962941578]),
urban = """color: #0b4a8b"""ee.FeatureCollection(
  [ee.Feature(
      ee.Geometry.Point([73.94571841157642, 15.367996652371586]),
      {
        "landcover": 0,
        "system:index": "0"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93992484010425, 15.369982923484374]),
      {
        "landcover": 0,
        "system:index": "1"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94249976075855, 15.3656379308444]),
      {
        "landcover": 0,
        "system:index": "2"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94863665498463, 15.364272343026814]),
      {
        "landcover": 0,
        "system:index": "3"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93790781892505, 15.366175887225985]),
      {
        "landcover": 0,
        "system:index": "4"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93095553315845, 15.369941543029237]),
      {
        "landcover": 0,
        "system:index": "5"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93194258607593, 15.372300215859992]),
      {
        "landcover": 0,
        "system:index": "6"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93164217866627, 15.371596754826639]),
      {
        "landcover": 0,
        "system:index": "7"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94945204652515, 15.373872649583744]),
      {
        "landcover": 0,
        "system:index": "8"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9541297600266, 15.360626378016411]),
      {
        "landcover": 0,
        "system:index": "9"
      }),
  ee.Feature(
      ee.Geometry.Point([73.95756298756567, 15.361122965121261]),
      {
        "landcover": 0,
        "system:index": "10"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9869032281606, 15.282680846171818]),
      {
        "landcover": 0,
        "system:index": "11"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98934940278218, 15.282887834743644]),
      {
        "landcover": 0,
        "system:index": "12"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98930648743794, 15.286820578783217]),
      {
        "landcover": 0,
        "system:index": "13"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97733310639546, 15.29004951347028]),
      {
        "landcover": 0,
        "system:index": "14"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97857765137837, 15.284626530679876]),
      {
        "landcover": 0,
        "system:index": "15"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98492912232564, 15.287731308987567]),
      {
        "landcover": 0,
        "system:index": "16"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97822013371206, 15.276843684331075]),
      {
        "landcover": 0,
        "system:index": "17"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97611728184438, 15.27464953184602]),
      {
        "landcover": 0,
        "system:index": "18"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97688975804067, 15.27796145130175]),
      {
        "landcover": 0,
        "system:index": "19"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98628821842885, 15.27808564726415]),
      {
        "landcover": 0,
        "system:index": "20"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9727698849938, 15.2710477600937]),
      {
        "landcover": 0,
        "system:index": "21"
      }),
  ee.Feature(
      ee.Geometry.Point([73.96603217594838, 15.270592359262752]),
      {
        "landcover": 0,
        "system:index": "22"
      }),
  ee.Feature(
      ee.Geometry.Point([73.96375766270376, 15.273448948131481]),
      {
        "landcover": 0,
        "system:index": "23"
      }),
  ee.Feature(
      ee.Geometry.Point([73.96028151982046, 15.271627359721968]),
      {
        "landcover": 0,
        "system:index": "24"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98367038243032, 15.275643113172853]),
      {
        "landcover": 0,
        "system:index": "25"
      }),
  ee.Feature(
      ee.Geometry.Point([73.99392714970327, 15.27692648208872]),
      {
        "landcover": 0,
        "system:index": "26"
      }),
  ee.Feature(
      ee.Geometry.Point([74.00341144077993, 15.270716559587386]),
      {
        "landcover": 0,
        "system:index": "27"
      }),
  ee.Feature(
      ee.Geometry.Point([74.00251021855092, 15.273407548570523]),
      {
        "landcover": 0,
        "system:index": "28"
      }),
  ee.Feature(
      ee.Geometry.Point([73.99963489048696, 15.27605710400355]),
      {
        "landcover": 0,
        "system:index": "29"
      }),
  ee.Feature(
      ee.Geometry.Point([74.01105037205434, 15.27593290684012]),
      {
        "landcover": 0,
        "system:index": "30"
      }),
  ee.Feature(
      ee.Geometry.Point([74.00276771061635, 15.283715786987646]),
      {
        "landcover": 0,
        "system:index": "31"
      }),
  ee.Feature(
      ee.Geometry.Point([74.01911845677114, 15.274318337024747]),
      {
        "landcover": 0,
        "system:index": "32"
      }),
  ee.Feature(
      ee.Geometry.Point([74.01555648319936, 15.26740452577731]),
      {
        "landcover": 0,
        "system:index": "33"
      }),
  ee.Feature(
      ee.Geometry.Point([74.0159427212975, 15.2631402052914]),
      {
        "landcover": 0,
        "system:index": "34"
      }),
  ee.Feature(
      ee.Geometry.Point([74.02070632450796, 15.262394975344884]),
      {
        "landcover": 0,
        "system:index": "35"
      }),
  ee.Feature(
      ee.Geometry.Point([74.01238074772573, 15.257592318916927]),
      {
        "landcover": 0,
        "system:index": "36"
      }),
  ee.Feature(
      ee.Geometry.Point([74.01482692234731, 15.257136888899607]),
      {
        "landcover": 0,
        "system:index": "37"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98748984806753, 15.259289822099907]),
      {
        "landcover": 0,
        "system:index": "38"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97817721836782, 15.260035063065963]),
      {
        "landcover": 0,
        "system:index": "39"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97397151463247, 15.256433040567005]),
      {
        "landcover": 0,
        "system:index": "40"
      }),
  ee.Feature(
      ee.Geometry.Point([73.99401298039174, 15.256184622945378]),
      {
        "landcover": 0,
        "system:index": "41"
      }),
  ee.Feature(
      ee.Geometry.Point([74.01834598057485, 15.261898153911154]),
      {
        "landcover": 0,
        "system:index": "42"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98129377107182, 15.240849273535162]),
      {
        "landcover": 0,
        "system:index": "43"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97193822602787, 15.247639744997514]),
      {
        "landcover": 0,
        "system:index": "44"
      }),
  ee.Feature(
      ee.Geometry.Point([73.99049911241093, 15.232112429792412]),
      {
        "landcover": 0,
        "system:index": "45"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98901853303471, 15.233064804787771]),
      {
        "landcover": 0,
        "system:index": "46"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98120794038334, 15.232008910511428]),
      {
        "landcover": 0,
        "system:index": "47"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81919894616885, 15.49103014792282]),
      {
        "landcover": 0,
        "system:index": "48"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81780419748111, 15.491216251313084]),
      {
        "landcover": 0,
        "system:index": "49"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81518636148257, 15.48827993384718]),
      {
        "landcover": 0,
        "system:index": "50"
      }),
  ee.Feature(
      ee.Geometry.Point([73.82419858377261, 15.489954880609792]),
      {
        "landcover": 0,
        "system:index": "51"
      }),
  ee.Feature(
      ee.Geometry.Point([73.82331881921573, 15.489251818189034]),
      {
        "landcover": 0,
        "system:index": "52"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81898436944766, 15.486501580458643]),
      {
        "landcover": 0,
        "system:index": "53"
      }),
  ee.Feature(
      ee.Geometry.Point([73.82868323724551, 15.488259255407296]),
      {
        "landcover": 0,
        "system:index": "54"
      }),
  ee.Feature(
      ee.Geometry.Point([73.80965028207584, 15.485633076733771]),
      {
        "landcover": 0,
        "system:index": "55"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8125256101398, 15.48615004367606]),
      {
        "landcover": 0,
        "system:index": "56"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81140097731691, 15.483928902841834]),
      {
        "landcover": 0,
        "system:index": "57"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8095985328589, 15.482150512038192]),
      {
        "landcover": 0,
        "system:index": "58"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81828889006715, 15.486120851863067]),
      {
        "landcover": 0,
        "system:index": "59"
      }),
  ee.Feature(
      ee.Geometry.Point([73.82062777632814, 15.483928902841834]),
      {
        "landcover": 0,
        "system:index": "60"
      }),
  ee.Feature(
      ee.Geometry.Point([73.82105692977052, 15.484859450075465]),
      {
        "landcover": 0,
        "system:index": "61"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8275371467505, 15.484011618321038]),
      {
        "landcover": 0,
        "system:index": "62"
      }),
  ee.Feature(
      ee.Geometry.Point([73.826320675136, 15.498114123747088]),
      {
        "landcover": 0,
        "system:index": "63"
      }),
  ee.Feature(
      ee.Geometry.Point([73.83164217782155, 15.496542631188245]),
      {
        "landcover": 0,
        "system:index": "64"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8343887598528, 15.496459920722524]),
      {
        "landcover": 0,
        "system:index": "65"
      }),
  ee.Feature(
      ee.Geometry.Point([73.83601954293385, 15.494474859614172]),
      {
        "landcover": 0,
        "system:index": "66"
      }),
  ee.Feature(
      ee.Geometry.Point([73.85558893990651, 15.491207738362402]),
      {
        "landcover": 0,
        "system:index": "67"
      }),
  ee.Feature(
      ee.Geometry.Point([73.85576060128346, 15.490546036630828]),
      {
        "landcover": 0,
        "system:index": "68"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87382796120778, 15.486906639251158]),
      {
        "landcover": 0,
        "system:index": "69"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87498667550221, 15.490091115461789]),
      {
        "landcover": 0,
        "system:index": "70"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86535218072072, 15.501711969598404]),
      {
        "landcover": 0,
        "system:index": "71"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86844208550588, 15.5027664987498]),
      {
        "landcover": 0,
        "system:index": "72"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88089462008486, 15.496790762386814]),
      {
        "landcover": 0,
        "system:index": "73"
      }),
  ee.Feature(
      ee.Geometry.Point([73.95496854317923, 15.58628534626265]),
      {
        "landcover": 0,
        "system:index": "74"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9547110511138, 15.585417262925953]),
      {
        "landcover": 0,
        "system:index": "75"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94690045846244, 15.586740055117724]),
      {
        "landcover": 0,
        "system:index": "76"
      }),
  ee.Feature(
      ee.Geometry.Point([73.96046170724173, 15.589509623677106]),
      {
        "landcover": 0,
        "system:index": "77"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9547110511138, 15.581283482425702]),
      {
        "landcover": 0,
        "system:index": "78"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97372254861136, 15.582027569054118]),
      {
        "landcover": 0,
        "system:index": "79"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97071847451468, 15.584879876164766]),
      {
        "landcover": 0,
        "system:index": "80"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94745835793753, 15.594511287177456]),
      {
        "landcover": 0,
        "system:index": "81"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94544133675834, 15.594511287177456]),
      {
        "landcover": 0,
        "system:index": "82"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94578465951224, 15.589261604134697]),
      {
        "landcover": 0,
        "system:index": "83"
      }),
  ee.Feature(
      ee.Geometry.Point([73.95711431039115, 15.597942109860684]),
      {
        "landcover": 0,
        "system:index": "84"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94505509866019, 15.598148784094603]),
      {
        "landcover": 0,
        "system:index": "85"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9387894584014, 15.602034220953717]),
      {
        "landcover": 0,
        "system:index": "86"
      }),
  ee.Feature(
      ee.Geometry.Point([73.80881505241632, 15.59438427335812]),
      {
        "landcover": 0,
        "system:index": "87"
      }),
  ee.Feature(
      ee.Geometry.Point([73.80306439628839, 15.598104442212549]),
      {
        "landcover": 0,
        "system:index": "88"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81756978264093, 15.598145777043289]),
      {
        "landcover": 0,
        "system:index": "89"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81568150749445, 15.59161477054599]),
      {
        "landcover": 0,
        "system:index": "90"
      }),
  ee.Feature(
      ee.Geometry.Point([73.80907254448175, 15.59264817148692]),
      {
        "landcover": 0,
        "system:index": "91"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8129349254632, 15.590664037086707]),
      {
        "landcover": 0,
        "system:index": "92"
      }),
  ee.Feature(
      ee.Geometry.Point([73.801734020617, 15.593061530406922]),
      {
        "landcover": 0,
        "system:index": "93"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8207884334588, 15.598311116282998]),
      {
        "landcover": 0,
        "system:index": "94"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81194787254572, 15.600873857464757]),
      {
        "landcover": 0,
        "system:index": "95"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8236272758611, 15.60368456905568]),
      {
        "landcover": 0,
        "system:index": "96"
      }),
  ee.Feature(
      ee.Geometry.Point([73.82731799546559, 15.606867240103572]),
      {
        "landcover": 0,
        "system:index": "97"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8135421699651, 15.606495242140008]),
      {
        "landcover": 0,
        "system:index": "98"
      }),
  ee.Feature(
      ee.Geometry.Point([73.80534533921559, 15.60583391076123]),
      {
        "landcover": 0,
        "system:index": "99"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81907080454516, 15.590912054935268]),
      {
        "landcover": 0,
        "system:index": "100"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81336306376147, 15.58971329922547]),
      {
        "landcover": 0,
        "system:index": "101"
      }),
  ee.Feature(
      ee.Geometry.Point([73.80010222239184, 15.588514536517833]),
      {
        "landcover": 0,
        "system:index": "102"
      }),
  ee.Feature(
      ee.Geometry.Point([73.80362128061938, 15.592193475713698]),
      {
        "landcover": 0,
        "system:index": "103"
      }),
  ee.Feature(
      ee.Geometry.Point([73.7965831641643, 15.589175923704621]),
      {
        "landcover": 0,
        "system:index": "104"
      }),
  ee.Feature(
      ee.Geometry.Point([73.81907080454516, 15.589217260333076]),
      {
        "landcover": 0,
        "system:index": "105"
      }),
  ee.Feature(
      ee.Geometry.Point([73.82662563645886, 15.581011776512083]),
      {
        "landcover": 0,
        "system:index": "106"
      }),
  ee.Feature(
      ee.Geometry.Point([73.82731228196667, 15.58138382065511]),
      {
        "landcover": 0,
        "system:index": "107"
      }),
  ee.Feature(
      ee.Geometry.Point([73.83276253068493, 15.568134500289126]),
      {
        "landcover": 0,
        "system:index": "108"
      }),
  ee.Feature(
      ee.Geometry.Point([73.79292482120388, 15.575600524449184]),
      {
        "landcover": 0,
        "system:index": "109"
      }),
  ee.Feature(
      ee.Geometry.Point([73.79867547733181, 15.57677869294716]),
      {
        "landcover": 0,
        "system:index": "110"
      }),
  ee.Feature(
      ee.Geometry.Point([73.7983321545779, 15.575972578388653]),
      {
        "landcover": 0,
        "system:index": "111"
      }),
  ee.Feature(
      ee.Geometry.Point([73.79835361225003, 15.57677869294716]),
      {
        "landcover": 0,
        "system:index": "112"
      }),
  ee.Feature(
      ee.Geometry.Point([73.79811757785671, 15.57894898565883]),
      {
        "landcover": 0,
        "system:index": "113"
      }),
  ee.Feature(
      ee.Geometry.Point([73.80075687152737, 15.577398778917678]),
      {
        "landcover": 0,
        "system:index": "114"
      })]),
    wr = """color: #ffc82d"""ee.FeatureCollection(
  [ee.Feature(
      ee.Geometry.Point([73.72350259509096, 15.49186943797597]),
      {
        "landcover": 1,
        "system:index": "0"
      }),
  ee.Feature(
      ee.Geometry.Point([73.70994134631167, 15.496170433831791]),
      {
        "landcover": 1,
        "system:index": "1"
      }),
  ee.Feature(
      ee.Geometry.Point([73.70170160021792, 15.488064636275162]),
      {
        "landcover": 1,
        "system:index": "2"
      }),
  ee.Feature(
      ee.Geometry.Point([73.73895211901674, 15.472348409327353]),
      {
        "landcover": 1,
        "system:index": "3"
      }),
  ee.Feature(
      ee.Geometry.Point([73.84784620756454, 15.506154030660646]),
      {
        "landcover": 1,
        "system:index": "4"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9949290239316, 15.514900785318734]),
      {
        "landcover": 1,
        "system:index": "5"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98939294452487, 15.518539689514052]),
      {
        "landcover": 1,
        "system:index": "6"
      }),
  ee.Feature(
      ee.Geometry.Point([73.99753691102364, 15.50791084695191]),
      {
        "landcover": 1,
        "system:index": "7"
      }),
  ee.Feature(
      ee.Geometry.Point([74.00324465180734, 15.49930925449602]),
      {
        "landcover": 1,
        "system:index": "8"
      }),
  ee.Feature(
      ee.Geometry.Point([74.01963831330636, 15.494677479446391]),
      {
        "landcover": 1,
        "system:index": "9"
      }),
  ee.Feature(
      ee.Geometry.Point([74.0315687790046, 15.478713602392657]),
      {
        "landcover": 1,
        "system:index": "10"
      }),
  ee.Feature(
      ee.Geometry.Point([74.03465868378976, 15.467298261374582]),
      {
        "landcover": 1,
        "system:index": "11"
      }),
  ee.Feature(
      ee.Geometry.Point([74.07192564023012, 15.480549222476949]),
      {
        "landcover": 1,
        "system:index": "12"
      }),
  ee.Feature(
      ee.Geometry.Point([74.07123899472231, 15.484188731736793]),
      {
        "landcover": 1,
        "system:index": "13"
      }),
  ee.Feature(
      ee.Geometry.Point([74.07922124875063, 15.467479547898211]),
      {
        "landcover": 1,
        "system:index": "14"
      }),
  ee.Feature(
      ee.Geometry.Point([74.05780649197573, 15.461027125851706]),
      {
        "landcover": 1,
        "system:index": "15"
      }),
  ee.Feature(
      ee.Geometry.Point([74.06814908993715, 15.462061181372416]),
      {
        "landcover": 1,
        "system:index": "16"
      }),
  ee.Feature(
      ee.Geometry.Point([74.05177620642962, 15.525936890556801]),
      {
        "landcover": 1,
        "system:index": "17"
      }),
  ee.Feature(
      ee.Geometry.Point([74.05520943396868, 15.529203462286084]),
      {
        "landcover": 1,
        "system:index": "18"
      }),
  ee.Feature(
      ee.Geometry.Point([74.04370812171283, 15.531477627239187]),
      {
        "landcover": 1,
        "system:index": "19"
      }),
  ee.Feature(
      ee.Geometry.Point([74.04679802649798, 15.53900286694067]),
      {
        "landcover": 1,
        "system:index": "20"
      }),
  ee.Feature(
      ee.Geometry.Point([74.03194931739154, 15.54218653947746]),
      {
        "landcover": 1,
        "system:index": "21"
      }),
  ee.Feature(
      ee.Geometry.Point([74.01319531195941, 15.555995666267748]),
      {
        "landcover": 1,
        "system:index": "22"
      }),
  ee.Feature(
      ee.Geometry.Point([73.99431256049456, 15.563437326519601]),
      {
        "landcover": 1,
        "system:index": "23"
      }),
  ee.Feature(
      ee.Geometry.Point([74.00602844947161, 15.562527804703976]),
      {
        "landcover": 1,
        "system:index": "24"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98663071387591, 15.550662310897945]),
      {
        "landcover": 1,
        "system:index": "25"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97298363440814, 15.550662310897945]),
      {
        "landcover": 1,
        "system:index": "26"
      }),
  ee.Feature(
      ee.Geometry.Point([73.95581749671283, 15.546858593209395]),
      {
        "landcover": 1,
        "system:index": "27"
      }),
  ee.Feature(
      ee.Geometry.Point([73.96259812110247, 15.540946153429614]),
      {
        "landcover": 1,
        "system:index": "28"
      }),
  ee.Feature(
      ee.Geometry.Point([73.96628884070697, 15.537514379788107]),
      {
        "landcover": 1,
        "system:index": "29"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97143868201556, 15.526184986427877]),
      {
        "landcover": 1,
        "system:index": "30"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97864845984759, 15.522951653668606]),
      {
        "landcover": 1,
        "system:index": "31"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9333059474069, 15.520532784327473]),
      {
        "landcover": 1,
        "system:index": "32"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93869559629638, 15.519984890534829]),
      {
        "landcover": 1,
        "system:index": "33"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94389908178528, 15.51908551455105]),
      {
        "landcover": 1,
        "system:index": "34"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92603556974609, 15.522817382383327]),
      {
        "landcover": 1,
        "system:index": "35"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93135707243164, 15.527613922214211]),
      {
        "landcover": 1,
        "system:index": "36"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92251651151855, 15.519013150795738]),
      {
        "landcover": 1,
        "system:index": "37"
      }),
  ee.Feature(
      ee.Geometry.Point([73.91934077604492, 15.512975856697516]),
      {
        "landcover": 1,
        "system:index": "38"
      }),
  ee.Feature(
      ee.Geometry.Point([73.91127269132812, 15.50685567971439]),
      {
        "landcover": 1,
        "system:index": "39"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90466372831543, 15.505366960586532]),
      {
        "landcover": 1,
        "system:index": "40"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89887015684326, 15.504084999405068]),
      {
        "landcover": 1,
        "system:index": "41"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88861338957031, 15.503216569567828]),
      {
        "landcover": 1,
        "system:index": "42"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87487065678033, 15.503257923452392]),
      {
        "landcover": 1,
        "system:index": "43"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86135232334527, 15.505284253653668]),
      {
        "landcover": 1,
        "system:index": "44"
      }),
  ee.Feature(
      ee.Geometry.Point([73.85877740269098, 15.507434623143581]),
      {
        "landcover": 1,
        "system:index": "45"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88070714359674, 15.518186134647031]),
      {
        "landcover": 1,
        "system:index": "46"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88941895847711, 15.527159082707476]),
      {
        "landcover": 1,
        "system:index": "47"
      }),
  ee.Feature(
      ee.Geometry.Point([73.898044942669, 15.536586460073659]),
      {
        "landcover": 1,
        "system:index": "48"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90469682102594, 15.53857111615775]),
      {
        "landcover": 1,
        "system:index": "49"
      }),
  ee.Feature(
      ee.Geometry.Point([73.91581189518365, 15.546716275269022]),
      {
        "landcover": 1,
        "system:index": "50"
      }),
  ee.Feature(
      ee.Geometry.Point([73.91787183170709, 15.544690352078149]),
      {
        "landcover": 1,
        "system:index": "51"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92980229740533, 15.537289361289378]),
      {
        "landcover": 1,
        "system:index": "52"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9359391916314, 15.540721138678444]),
      {
        "landcover": 1,
        "system:index": "53"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94216191654596, 15.544897079847317]),
      {
        "landcover": 1,
        "system:index": "54"
      })]),
    vtation = """color: #00ffff"""ee.FeatureCollection(
  [ee.Feature(
      ee.Geometry.Point([73.996326542225, 15.484125707986706]),
      {
        "landcover": 2,
        "system:index": "0"
      }),
  ee.Feature(
      ee.Geometry.Point([73.99031839403165, 15.48379484605395]),
      {
        "landcover": 2,
        "system:index": "1"
      }),
  ee.Feature(
      ee.Geometry.Point([74.00164804491055, 15.479080006007997]),
      {
        "landcover": 2,
        "system:index": "2"
      }),
  ee.Feature(
      ee.Geometry.Point([73.98619852098477, 15.469898167067473]),
      {
        "landcover": 2,
        "system:index": "3"
      }),
  ee.Feature(
      ee.Geometry.Point([73.97847375902188, 15.48379484605395]),
      {
        "landcover": 2,
        "system:index": "4"
      }),
  ee.Feature(
      ee.Geometry.Point([74.06413278612149, 15.50786366964528]),
      {
        "landcover": 2,
        "system:index": "5"
      }),
  ee.Feature(
      ee.Geometry.Point([74.05958375963223, 15.515058958987987]),
      {
        "landcover": 2,
        "system:index": "6"
      }),
  ee.Feature(
      ee.Geometry.Point([74.07589159044278, 15.50438999194169]),
      {
        "landcover": 2,
        "system:index": "7"
      }),
  ee.Feature(
      ee.Geometry.Point([74.07443246873868, 15.510344832229498]),
      {
        "landcover": 2,
        "system:index": "8"
      }),
  ee.Feature(
      ee.Geometry.Point([74.0959759715463, 15.526223566500466]),
      {
        "landcover": 2,
        "system:index": "9"
      }),
  ee.Feature(
      ee.Geometry.Point([74.10498819383633, 15.530275756052484]),
      {
        "landcover": 2,
        "system:index": "10"
      }),
  ee.Feature(
      ee.Geometry.Point([74.08807954820645, 15.532177776746598]),
      {
        "landcover": 2,
        "system:index": "11"
      }),
  ee.Feature(
      ee.Geometry.Point([74.10816392930997, 15.518449755518551]),
      {
        "landcover": 2,
        "system:index": "12"
      }),
  ee.Feature(
      ee.Geometry.Point([74.11700449022305, 15.52159239523332]),
      {
        "landcover": 2,
        "system:index": "13"
      }),
  ee.Feature(
      ee.Geometry.Point([74.12028294992058, 15.537569233902616]),
      {
        "landcover": 2,
        "system:index": "14"
      }),
  ee.Feature(
      ee.Geometry.Point([74.10414678048699, 15.542530814607678]),
      {
        "landcover": 2,
        "system:index": "15"
      }),
  ee.Feature(
      ee.Geometry.Point([74.11857797253151, 15.554768869372356]),
      {
        "landcover": 2,
        "system:index": "16"
      }),
  ee.Feature(
      ee.Geometry.Point([74.12355615246315, 15.548153794950062]),
      {
        "landcover": 2,
        "system:index": "17"
      }),
  ee.Feature(
      ee.Geometry.Point([74.12038041698952, 15.564525716089372]),
      {
        "landcover": 2,
        "system:index": "18"
      }),
  ee.Feature(
      ee.Geometry.Point([74.10106851208229, 15.557993641079932]),
      {
        "landcover": 2,
        "system:index": "19"
      }),
  ee.Feature(
      ee.Geometry.Point([74.09368707287331, 15.558159012625959]),
      {
        "landcover": 2,
        "system:index": "20"
      }),
  ee.Feature(
      ee.Geometry.Point([74.09428788769264, 15.547161515456374]),
      {
        "landcover": 2,
        "system:index": "21"
      }),
  ee.Feature(
      ee.Geometry.Point([74.1149730836155, 15.560474200316387]),
      {
        "landcover": 2,
        "system:index": "22"
      }),
  ee.Feature(
      ee.Geometry.Point([74.11660386669655, 15.573537985370383]),
      {
        "landcover": 2,
        "system:index": "23"
      }),
  ee.Feature(
      ee.Geometry.Point([74.14398385632057, 15.575026212020406]),
      {
        "landcover": 2,
        "system:index": "24"
      }),
  ee.Feature(
      ee.Geometry.Point([74.12132455456276, 15.585443496827775]),
      {
        "landcover": 2,
        "system:index": "25"
      }),
  ee.Feature(
      ee.Geometry.Point([74.10510255444069, 15.594620191007278]),
      {
        "landcover": 2,
        "system:index": "26"
      }),
  ee.Feature(
      ee.Geometry.Point([74.0889663850071, 15.592388059898559]),
      {
        "landcover": 2,
        "system:index": "27"
      }),
  ee.Feature(
      ee.Geometry.Point([74.10098268139382, 15.598753703043561]),
      {
        "landcover": 2,
        "system:index": "28"
      }),
  ee.Feature(
      ee.Geometry.Point([74.08321572887917, 15.590486595738996]),
      {
        "landcover": 2,
        "system:index": "29"
      }),
  ee.Feature(
      ee.Geometry.Point([74.0820140992405, 15.603383137686698]),
      {
        "landcover": 2,
        "system:index": "30"
      }),
  ee.Feature(
      ee.Geometry.Point([74.10596086132546, 15.602639128449027]),
      {
        "landcover": 2,
        "system:index": "31"
      }),
  ee.Feature(
      ee.Geometry.Point([74.0750618134739, 15.593958821357026]),
      {
        "landcover": 2,
        "system:index": "32"
      }),
  ee.Feature(
      ee.Geometry.Point([74.07557679760475, 15.588089072354322]),
      {
        "landcover": 2,
        "system:index": "33"
      }),
  ee.Feature(
      ee.Geometry.Point([74.06622125256081, 15.599911071495855]),
      {
        "landcover": 2,
        "system:index": "34"
      }),
  ee.Feature(
      ee.Geometry.Point([74.11033822643776, 15.604705814113897]),
      {
        "landcover": 2,
        "system:index": "35"
      }),
  ee.Feature(
      ee.Geometry.Point([74.09308625805397, 15.610244429020867]),
      {
        "landcover": 2,
        "system:index": "36"
      }),
  ee.Feature(
      ee.Geometry.Point([74.09669114696999, 15.6349597073728]),
      {
        "landcover": 2,
        "system:index": "37"
      }),
  ee.Feature(
      ee.Geometry.Point([74.0933437501194, 15.637935258811781]),
      {
        "landcover": 2,
        "system:index": "38"
      }),
  ee.Feature(
      ee.Geometry.Point([74.07386018383522, 15.632645359686851]),
      {
        "landcover": 2,
        "system:index": "39"
      }),
  ee.Feature(
      ee.Geometry.Point([74.10227014172096, 15.64545659873638]),
      {
        "landcover": 2,
        "system:index": "40"
      }),
  ee.Feature(
      ee.Geometry.Point([74.11754800426979, 15.646861653568058]),
      {
        "landcover": 2,
        "system:index": "41"
      }),
  ee.Feature(
      ee.Geometry.Point([74.12827684032936, 15.643472975487326]),
      {
        "landcover": 2,
        "system:index": "42"
      }),
  ee.Feature(
      ee.Geometry.Point([74.14209558117409, 15.647605502219076]),
      {
        "landcover": 2,
        "system:index": "43"
      }),
  ee.Feature(
      ee.Geometry.Point([74.10930825817604, 15.653225604591878]),
      {
        "landcover": 2,
        "system:index": "44"
      }),
  ee.Feature(
      ee.Geometry.Point([74.11909295666237, 15.657192642681336]),
      {
        "landcover": 2,
        "system:index": "45"
      }),
  ee.Feature(
      ee.Geometry.Point([74.15840341198464, 15.647936100751272]),
      {
        "landcover": 2,
        "system:index": "46"
      }),
  ee.Feature(
      ee.Geometry.Point([74.16209413158913, 15.642481156651156]),
      {
        "landcover": 2,
        "system:index": "47"
      }),
  ee.Feature(
      ee.Geometry.Point([74.17007638561745, 15.646200452496428]),
      {
        "landcover": 2,
        "system:index": "48"
      }),
  ee.Feature(
      ee.Geometry.Point([74.15333940136452, 15.642481156651156]),
      {
        "landcover": 2,
        "system:index": "49"
      }),
  ee.Feature(
      ee.Geometry.Point([74.17745782482643, 15.639670977176177]),
      {
        "landcover": 2,
        "system:index": "50"
      }),
  ee.Feature(
      ee.Geometry.Point([74.18475343334694, 15.644547440467827]),
      {
        "landcover": 2,
        "system:index": "51"
      }),
  ee.Feature(
      ee.Geometry.Point([74.1904182587864, 15.640580157111447]),
      {
        "landcover": 2,
        "system:index": "52"
      }),
  ee.Feature(
      ee.Geometry.Point([74.20294953930397, 15.645125996197082]),
      {
        "landcover": 2,
        "system:index": "53"
      }),
  ee.Feature(
      ee.Geometry.Point([74.20097543346901, 15.637274028896515]),
      {
        "landcover": 2,
        "system:index": "54"
      }),
  ee.Feature(
      ee.Geometry.Point([74.19282151806374, 15.627933928215574]),
      {
        "landcover": 2,
        "system:index": "55"
      }),
  ee.Feature(
      ee.Geometry.Point([74.18449594128151, 15.627603297375803]),
      {
        "landcover": 2,
        "system:index": "56"
      }),
  ee.Feature(
      ee.Geometry.Point([74.19977380383034, 15.625040890272636]),
      {
        "landcover": 2,
        "system:index": "57"
      }),
  ee.Feature(
      ee.Geometry.Point([74.17419625866432, 15.625123549066583]),
      {
        "landcover": 2,
        "system:index": "58"
      }),
  ee.Feature(
      ee.Geometry.Point([74.21067430126686, 15.632893326761623]),
      {
        "landcover": 2,
        "system:index": "59"
      }),
  ee.Feature(
      ee.Geometry.Point([74.21058847057839, 15.626776717941462]),
      {
        "landcover": 2,
        "system:index": "60"
      }),
  ee.Feature(
      ee.Geometry.Point([74.20586778271218, 15.61652685589641]),
      {
        "landcover": 2,
        "system:index": "61"
      }),
  ee.Feature(
      ee.Geometry.Point([74.19204904186745, 15.610161764226245]),
      {
        "landcover": 2,
        "system:index": "62"
      })]),
    fds = """color: #bf04c2"""ee.FeatureCollection(
  [ee.Feature(
      ee.Geometry.Point([73.94153829715492, 15.486271921182173]),
      {
        "landcover": 3,
        "system:index": "0"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94074436328651, 15.484617623392841]),
      {
        "landcover": 3,
        "system:index": "1"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94400592944862, 15.484762374977693]),
      {
        "landcover": 3,
        "system:index": "2"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9376973738456, 15.482777201552988]),
      {
        "landcover": 3,
        "system:index": "3"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93525119922401, 15.482032756606541]),
      {
        "landcover": 3,
        "system:index": "4"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92769809863807, 15.483521643820124]),
      {
        "landcover": 3,
        "system:index": "5"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92971511981727, 15.484100652619919]),
      {
        "landcover": 3,
        "system:index": "6"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92885681293251, 15.48091608416343]),
      {
        "landcover": 3,
        "system:index": "7"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93070217273475, 15.482363621357957]),
      {
        "landcover": 3,
        "system:index": "8"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90718456409218, 15.524627237452924]),
      {
        "landcover": 3,
        "system:index": "9"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90975948474647, 15.525040733031249]),
      {
        "landcover": 3,
        "system:index": "10"
      }),
  ee.Feature(
      ee.Geometry.Point([73.91229149005653, 15.526529310249092]),
      {
        "landcover": 3,
        "system:index": "11"
      }),
  ee.Feature(
      ee.Geometry.Point([73.91872879169227, 15.523965642803402]),
      {
        "landcover": 3,
        "system:index": "12"
      }),
  ee.Feature(
      ee.Geometry.Point([73.91134735248329, 15.522352996955107]),
      {
        "landcover": 3,
        "system:index": "13"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90336509845497, 15.522063546365802]),
      {
        "landcover": 3,
        "system:index": "14"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90027519366981, 15.519954679814276]),
      {
        "landcover": 3,
        "system:index": "15"
      }),
  ee.Feature(
      ee.Geometry.Point([73.91812797687294, 15.51887956308046]),
      {
        "landcover": 3,
        "system:index": "16"
      }),
  ee.Feature(
      ee.Geometry.Point([73.91190525195839, 15.5176390368113]),
      {
        "landcover": 3,
        "system:index": "17"
      }),
  ee.Feature(
      ee.Geometry.Point([73.91284938953163, 15.52115384186975]),
      {
        "landcover": 3,
        "system:index": "18"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89920231006386, 15.5161503954443]),
      {
        "landcover": 3,
        "system:index": "19"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89830108783485, 15.517804440744737]),
      {
        "landcover": 3,
        "system:index": "20"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93821235797645, 15.535088420713079]),
      {
        "landcover": 3,
        "system:index": "21"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9247476687217, 15.534395848901418]),
      {
        "landcover": 3,
        "system:index": "22"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92550941608192, 15.534571576297841]),
      {
        "landcover": 3,
        "system:index": "23"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92612095973732, 15.534623260797682]),
      {
        "landcover": 3,
        "system:index": "24"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92678614757301, 15.534654271491366]),
      {
        "landcover": 3,
        "system:index": "25"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92698999545814, 15.533661926979313]),
      {
        "landcover": 3,
        "system:index": "26"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92636772296669, 15.533114068066478]),
      {
        "landcover": 3,
        "system:index": "27"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92589565418007, 15.533114068066478]),
      {
        "landcover": 3,
        "system:index": "28"
      }),
  ee.Feature(
      ee.Geometry.Point([73.92574545047523, 15.533651590032164]),
      {
        "landcover": 3,
        "system:index": "29"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9356803526664, 15.536339178834679]),
      {
        "landcover": 3,
        "system:index": "30"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93984314105751, 15.539398852654942]),
      {
        "landcover": 3,
        "system:index": "31"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9400577177787, 15.538096429487274]),
      {
        "landcover": 3,
        "system:index": "32"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94123788974525, 15.536401199701016]),
      {
        "landcover": 3,
        "system:index": "33"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93937107227089, 15.536669956572885]),
      {
        "landcover": 3,
        "system:index": "34"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94381281039955, 15.536359852458862]),
      {
        "landcover": 3,
        "system:index": "35"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94660230777504, 15.537021407338031]),
      {
        "landcover": 3,
        "system:index": "36"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9472245802665, 15.535718969144593]),
      {
        "landcover": 3,
        "system:index": "37"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9462160696769, 15.535718969144593]),
      {
        "landcover": 3,
        "system:index": "38"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9431905379081, 15.532121716139763]),
      {
        "landcover": 3,
        "system:index": "39"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94537922046425, 15.533754959480257]),
      {
        "landcover": 3,
        "system:index": "40"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94188161990883, 15.533692937817623]),
      {
        "landcover": 3,
        "system:index": "41"
      }),
  ee.Feature(
      ee.Geometry.Point([73.94100185535194, 15.532948676410426]),
      {
        "landcover": 3,
        "system:index": "42"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93866296909096, 15.533754959480257]),
      {
        "landcover": 3,
        "system:index": "43"
      }),
  ee.Feature(
      ee.Geometry.Point([73.93731113574745, 15.531522167869193]),
      {
        "landcover": 3,
        "system:index": "44"
      }),
  ee.Feature(
      ee.Geometry.Point([73.892743550756, 15.555358036089846]),
      {
        "landcover": 3,
        "system:index": "45"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89104839465858, 15.555936843331844]),
      {
        "landcover": 3,
        "system:index": "46"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8909625639701, 15.556991095197308]),
      {
        "landcover": 3,
        "system:index": "47"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89220710895302, 15.555068631858472]),
      {
        "landcover": 3,
        "system:index": "48"
      }),
  ee.Feature(
      ee.Geometry.Point([73.889503442266, 15.557032438297679]),
      {
        "landcover": 3,
        "system:index": "49"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90128370425941, 15.55306346279363]),
      {
        "landcover": 3,
        "system:index": "50"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90214201114418, 15.554117729376191]),
      {
        "landcover": 3,
        "system:index": "51"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90010353229286, 15.554345119499843]),
      {
        "landcover": 3,
        "system:index": "52"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90136953494789, 15.556722364842473]),
      {
        "landcover": 3,
        "system:index": "53"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90018936298134, 15.55951300912072]),
      {
        "landcover": 3,
        "system:index": "54"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90388008258583, 15.56116670639031]),
      {
        "landcover": 3,
        "system:index": "55"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90885826251747, 15.56178683943979]),
      {
        "landcover": 3,
        "system:index": "56"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90881534717323, 15.560257174536765]),
      {
        "landcover": 3,
        "system:index": "57"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8971745600486, 15.568494492454935]),
      {
        "landcover": 3,
        "system:index": "58"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89753934047462, 15.568990581370766]),
      {
        "landcover": 3,
        "system:index": "59"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89888044498207, 15.567688345414298]),
      {
        "landcover": 3,
        "system:index": "60"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89943834445717, 15.568773542617341]),
      {
        "landcover": 3,
        "system:index": "61"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89978166721107, 15.56940398788642]),
      {
        "landcover": 3,
        "system:index": "62"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89995332858803, 15.569920744862257]),
      {
        "landcover": 3,
        "system:index": "63"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89941688678505, 15.567864044397606]),
      {
        "landcover": 3,
        "system:index": "64"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89968510768654, 15.567316276483592]),
      {
        "landcover": 3,
        "system:index": "65"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89803286693336, 15.569858734093721]),
      {
        "landcover": 3,
        "system:index": "66"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89660593173744, 15.569848398963813]),
      {
        "landcover": 3,
        "system:index": "67"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90273209712745, 15.571429667799121]),
      {
        "landcover": 3,
        "system:index": "68"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90238877437355, 15.572618195192694]),
      {
        "landcover": 3,
        "system:index": "69"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90251752040626, 15.569858734093721]),
      {
        "landcover": 3,
        "system:index": "70"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90332218311073, 15.56948666908983]),
      {
        "landcover": 3,
        "system:index": "71"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90365477702858, 15.568515162850309]),
      {
        "landcover": 3,
        "system:index": "72"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90246387622597, 15.568639185179002]),
      {
        "landcover": 3,
        "system:index": "73"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90201326511146, 15.573910065001302]),
      {
        "landcover": 3,
        "system:index": "74"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90026446483375, 15.577237884234304]),
      {
        "landcover": 3,
        "system:index": "75"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9016592135215, 15.575915030866726]),
      {
        "landcover": 3,
        "system:index": "76"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90212055347206, 15.577651274165579]),
      {
        "landcover": 3,
        "system:index": "77"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90413757465126, 15.576586793406449]),
      {
        "landcover": 3,
        "system:index": "78"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90339728496315, 15.57715520614827]),
      {
        "landcover": 3,
        "system:index": "79"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90183087489845, 15.578498720925198]),
      {
        "landcover": 3,
        "system:index": "80"
      }),
  ee.Feature(
      ee.Geometry.Point([73.9002000918174, 15.57858139847074]),
      {
        "landcover": 3,
        "system:index": "81"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89989968440773, 15.579180809681223]),
      {
        "landcover": 3,
        "system:index": "82"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90074726245643, 15.58000758089568]),
      {
        "landcover": 3,
        "system:index": "83"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8991915812278, 15.580968698251274]),
      {
        "landcover": 3,
        "system:index": "84"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89817234180214, 15.579790553773876]),
      {
        "landcover": 3,
        "system:index": "85"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89371987483742, 15.581609440657402]),
      {
        "landcover": 3,
        "system:index": "86"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89468547008278, 15.581588771578728]),
      {
        "landcover": 3,
        "system:index": "87"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8957690825248, 15.582281184582852]),
      {
        "landcover": 3,
        "system:index": "88"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89590855739357, 15.58142341887437]),
      {
        "landcover": 3,
        "system:index": "89"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89668103358986, 15.582157170484999]),
      {
        "landcover": 3,
        "system:index": "90"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89839764735939, 15.583231956846161]),
      {
        "landcover": 3,
        "system:index": "91"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89947053096535, 15.583376639196166]),
      {
        "landcover": 3,
        "system:index": "92"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89830108783485, 15.582973595253465]),
      {
        "landcover": 3,
        "system:index": "93"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90153046748878, 15.583273294670848]),
      {
        "landcover": 3,
        "system:index": "94"
      }),
  ee.Feature(
      ee.Geometry.Point([73.90015717647316, 15.582653226427293]),
      {
        "landcover": 3,
        "system:index": "95"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89954563281776, 15.583004598661743]),
      {
        "landcover": 3,
        "system:index": "96"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89612313411476, 15.582157170484999]),
      {
        "landcover": 3,
        "system:index": "97"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88940688274147, 15.579904234675789]),
      {
        "landcover": 3,
        "system:index": "98"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89090891978981, 15.580265946218036]),
      {
        "landcover": 3,
        "system:index": "99"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88866659305336, 15.580762006726284]),
      {
        "landcover": 3,
        "system:index": "100"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89023300311806, 15.580844683361232]),
      {
        "landcover": 3,
        "system:index": "101"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8876473536277, 15.579439176043072]),
      {
        "landcover": 3,
        "system:index": "102"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88888116977455, 15.57838503924574]),
      {
        "landcover": 3,
        "system:index": "103"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89042612216713, 15.57875708814459]),
      {
        "landcover": 3,
        "system:index": "104"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89037247798683, 15.578261022796466]),
      {
        "landcover": 3,
        "system:index": "105"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88761516711952, 15.57831269632609]),
      {
        "landcover": 3,
        "system:index": "106"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89058705470802, 15.577124201857428]),
      {
        "landcover": 3,
        "system:index": "107"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89226075313331, 15.577857968819409]),
      {
        "landcover": 3,
        "system:index": "108"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88497587344887, 15.579036124376701]),
      {
        "landcover": 3,
        "system:index": "109"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88560887477638, 15.579046459044678]),
      {
        "landcover": 3,
        "system:index": "110"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88480421207191, 15.577630604688776]),
      {
        "landcover": 3,
        "system:index": "111"
      }),
  ee.Feature(
      ee.Geometry.Point([73.88214346072914, 15.579201479002126]),
      {
        "landcover": 3,
        "system:index": "112"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89775391719581, 15.577868303546646]),
      {
        "landcover": 3,
        "system:index": "113"
      }),
  ee.Feature(
      ee.Geometry.Point([73.89775391719581, 15.577868303546646]),
      {
        "landcover": 3,
        "system:index": "114"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87395736912322, 15.571284978202504]),
      {
        "landcover": 3,
        "system:index": "115"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8749444220407, 15.571284978202504]),
      {
        "landcover": 3,
        "system:index": "116"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87268063763213, 15.572070441107046]),
      {
        "landcover": 3,
        "system:index": "117"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87137171963286, 15.572070441107046]),
      {
        "landcover": 3,
        "system:index": "118"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87376425007415, 15.570850905310031]),
      {
        "landcover": 3,
        "system:index": "119"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87266990879607, 15.570943921006997]),
      {
        "landcover": 3,
        "system:index": "120"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87560960987639, 15.57056152287262]),
      {
        "landcover": 3,
        "system:index": "121"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87441870907378, 15.571822400513996]),
      {
        "landcover": 3,
        "system:index": "122"
      }),
  ee.Feature(
      ee.Geometry.Point([73.87530920246672, 15.570096443102113]),
      {
        "landcover": 3,
        "system:index": "123"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8610934946878, 15.56683051997495]),
      {
        "landcover": 3,
        "system:index": "124"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86119005421233, 15.567678011339252]),
      {
        "landcover": 3,
        "system:index": "125"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8628959391458, 15.566179396188712]),
      {
        "landcover": 3,
        "system:index": "126"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86374351719451, 15.566396437679828]),
      {
        "landcover": 3,
        "system:index": "127"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86315343121123, 15.565342234006145]),
      {
        "landcover": 3,
        "system:index": "128"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86555669048857, 15.56542491684249]),
      {
        "landcover": 3,
        "system:index": "129"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86292812565398, 15.564587751589173]),
      {
        "landcover": 3,
        "system:index": "130"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86573908070159, 15.56673750241741]),
      {
        "landcover": 3,
        "system:index": "131"
      }),
  ee.Feature(
      ee.Geometry.Point([73.8653099272592, 15.566820184692856]),
      {
        "landcover": 3,
        "system:index": "132"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86655447224211, 15.56768834657823]),
      {
        "landcover": 3,
        "system:index": "133"
      }),
  ee.Feature(
      ee.Geometry.Point([73.86526701191497, 15.564970160831306]),
      {
        "landcover": 3,
        "system:index": "134"
      })])