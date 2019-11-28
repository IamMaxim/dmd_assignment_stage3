import datetime
from random import randrange, random, choice, randint, sample

num_of_patients = 200

fem_name = ['Hana', 'Zoya', 'Willie', 'Nettie', 'Kara', 'Lara', 'Halima', 'Laila', 'Alicia', 'Caroline', 'Carla',
            'Julie',
            'Katherine', 'Holly', 'Rebekah', 'Lachlan', 'Lachlan', 'Millie', 'Chantelle', 'Robin', 'Aminah', 'Ashley',
            'Fern',
            'Agnes', 'Harley', 'Rhiannon']
male_name = ['Hamzah', 'Courtney', 'Theo', 'Victor', 'Bruce', 'Rafael', 'Barnaby', 'Anita', 'Vincent', 'Ismail',
             'Verity', 'Abby', 'Gary', 'Lewis', 'Simon', 'Jean', 'John', 'James', 'Egor', 'Nick',
             'Joseph', 'Artem', 'Peter', 'Igor', 'Alex']

surnames = ['Hughes', 'Cassidy', 'Farmer', 'Chavez', 'Santiago', 'Payne', 'Rice', 'Li', 'Hamilton', 'Singh', 'Simmons',
            'Little', 'Mcdaniel', 'Ramsey', 'Garner', 'Harrison', 'Fernandez', 'Strickland', 'Read', 'Gilbert', 'Owen',
            'Maxwell', 'Schwartz', 'Crawford', 'Hubbard', 'Gibbs', 'Wilkes', 'Connor', 'Lindsey', 'Greene', 'Fisher',
            'Park', 'Ortega', 'Manning', 'Logan', 'Woodward', 'Lewis', 'Huff', 'Gill', 'Terry', 'Riley', 'Powers',
            'Cole', 'Flores', 'Huang', 'Barrett', 'Cannon', 'Carr']

staff_position = ['cleaning manager', 'accountant', 'security guard',
                  'CEO', 'HR', 'fMRI technologist', 'engineer', 'pharmacist',
                  'schedule manager', 'PR manager', 'lawyer', 'storage manager']

chat_names = ['Reschedule', 'Surgeons', 'Nurses in surgeon', 'Administrative', 'All hospital staff', 'Some stuff',
              'Nurses with kids', 'therapists', 'dentists', 'dermatologists', 'urologists', 'venereologists',
              'regional ambulance', 'ambulances in south district', 'ambulances in north district',
              'ambulances in west district', 'ambulances in east district', 'accounting', 'cleaning service',
              'lawyers']

chat_message = ['hello', 'we need help', 'Mary, come to the 338, please',
                'We need a cleaning manager in 505',
                'have a nice day', 'today its turkey in the canteen', 'has anyone diagnosed a new patient?',
                'Urgernt, there is an insult at 666',
                'can anyone take my patients on 25th of november as I feel bad',
                'dear collegues, I need your advice', 'the is a new patient in 228',
                'Kate, let me know when the man from 123 will move away from anesthesia',
                'who gave opiates to Irek James? He has an allergy on this type of painkillers',
                'Have a nice weekend', 'Dear Mr Rogers, have a nice birthday', 'Thanks',
                'Who is on duty tonight?', 'John, please look thorough his digital medical file',
                'According to the shift timetable you had an emergency call on 21th of November. Could you provide me more details about that case please?',
                'Good day, can we exhange a shifts on 2nd of December my daughter\'\'s birthday is that day. I will take your turn at 3',
                'I accidentally lost Petrov\'\'s blood analysis results. Can you please check if they are still I laboratory.',
                'Can you please have a lock on Ivanov\'\'s results. Some strange things happening there.',
                'Don\'\'t forget about obligatory meeting with head of the hospital tomorrow at 9am.',
                'I will send you eeg of patient can you have a look and tell me your opinion?',
                'I would like to request the time in laboratory tomorrow.',
                'I have a really hard case. Could you please assist me on operation 23th of November. I don\'\'t think I am able to do it alone.',
                'What is your opinion about this new pills Korpex? Should I recommend them to patients?',
                'The head of hospital told me that you had a promotion. Congratulations!'
                ]

amb_loc = [
    'Part Lane', 'Hampshire Woods', 'Ty Du Road', 'East Maltings', 'Primrose Grange', 'Shetland Mount',
    'Hollybush Quay', 'Stockton Furlong', 'Brooklands Oak', 'Sea Oval', 'Rosslyn Parkway', 'Ash Meadow', 'Booth Hill',
    'Garth Point', 'Baxter Mead', 'Chesterfield Corner', 'Claremont Celyn', 'Malton Woodlands', 'Irvine Hill',
    'Alpine Maltings', 'Holbrook Way', 'Alexandra Esplanade', 'Roseburn Maltings', 'Wallis Acres', 'Foxglove Holt',
    'Queensby Place', 'Church Covert', 'Hartley North', 'Christopher Gardens', 'Nene Bank', 'Argyle Mount',
    'Hatfield Lodge', 'Fold Hill', 'Alpine Mead', 'Argyle Fairway', 'Hobart Lanes', 'Plover Reach',
    'St Owains Crescent', 'Cliff Hey', 'Cobbler Hall', 'Coventry Oaks', 'Brooklands Moor', 'Bluegown Avenue',
    'Argyll Pleasant', 'Windlass Drive', 'Ashwood Park Road', 'Sherwood Path', 'Curlew Acre', 'Edward Heath',
    'Wharfedale Pleasant', 'Kingsmead Street', 'Snakehill Lane', 'Munro Corner', 'Winston Laurels', 'Lenny Balk',
    'Bloomfield Limes', 'Epsom Oak', 'Eastfield Elms', 'Kinnersley Avenue', 'Chandlers Side', 'Southern Edge',
    'Ardwell Close', 'Kirkby Farm', 'Paterson Moor', 'Brown\'\'s Way', 'Dean Park Brae', 'The Furlong',
    'Bridgewater View', 'Mincing Lane', 'Howe Covert', 'Links Hollies', 'Kipling Buildings', 'Cheyne Field',
    'Staker Lane', 'Foxes Birches', 'Lime Lodge', 'Overdale Gait', 'Chelmsford Beeches', 'Woods Estate',
    'Wykeham Rowans', 'Burleigh East', 'Barn Hollies', 'John Hammond Close', 'Oakland Lawn', 'Harvest Woodlands',
    'Rosehill Top', 'The Four Wents', 'Ward Cross', 'Winston Lea', 'Coed Bach', 'Borrowdale Acres', 'Surrey Manor',
    'Mcleod\'\'s Mews', 'Stanford Esplanade', 'Lavender Bank', 'Neville Banks', 'Belvoir Brae', 'Sherborne Downs',
    'Links Paddock', 'Davies Promenade']

doc_specialization = ['Family Physician', 'Internal Medicine Physician', 'Pediatrician',
                      'Obstetrician/Gynecologist (OB/GYN)', 'Surgeon', 'Psychiatrist', 'Cardiologist', 'Dermatologist',
                      'Endocrinologist', 'Gastroenterologist', 'Infectious Disease Physician', 'Nephrologist',
                      'Ophthalmologist', 'Otolaryngologist', 'Pulmonologist', 'Neurologist', 'Physician Executive',
                      'Radiologist', 'Anesthesiologist', 'Oncologist']

inventory_name = ['Calcium Antagonists pills', 'antiviral pills', 'contraceptive pills', 'Drotaverinum', 'antibiotics',
                  'EEG', 'fMRI', 'gramidine', 'strepsils', 'paracetamol', 'vitamins', 'ferrum',
                  'magnesium', 'sedative', 'sleeping pil', 'x-ray', 'pet', 'blood tester', 'physiotherapy equipment',
                  'holter', 'urine test', 'painkiller', 'noshpa', 'analgetic', 'tranquilizer', 'ACE inhibitors',
                  'Diuretics', 'Beta-blockers', 'Alpha-2 Receptor Agonists', 'modafinil (Provigil)',
                  'methylphenidate (Ritalin)', 'memantine (Axura)'
                  ]

inventory_supplier = ['General Electrics', 'BAYER AG', 'Roche', 'biocad', 'biogen', 'amgen',
                      'Lisapharma', 'Medicuba', 'Meditech', 'Novartis Pharma AG',
                      'Merck Serono', 'msd', 'Teva Pharmaceutical Industries Ltd', 'AstraZeneca',
                      'Veropharm', 'Bristol-Myers Squibb', 'Astellas Pharma Europe B.V.', 'Pfizer International LLC'
                      ]

inventory_instruction = [
    'Corticosteroids? Prescription corticosteroids provide relief for inflamed areas of the body\
     by easing swelling, redness, itching and allergic reactions. Corticosteroids can be used to\
      treat allergies, asthma and arthritis. When used to control pain, they are generally given in\
       the form of pills or injections that target a certain joint. Examples include: prednisone, \
       prednisolone, and methylprednisolone.Prescription corticosteroids are strong medicines and\
        may have serious side effects, including:Weight gain and salt retention,Peptic ulcer disease,\
        Mood changes,Trouble sleeping,Weakened immune system,Thinning of the bones and skin, High sugar\
         levels. To minimize these potential side effects, corticosteroids are prescribed in the\
          lowest dose possible for as short of a length of time as needed to relieve the pain.',

    'Oral-Adults: 1 to 2 tablets, 3 times daily Children (over 6 years):\
     1/2 to 1 tablet, 1-2 times daily.Children (1-6 years): 1/4 to 1/2 tablet, 1-2 times daily.',

    'Injection-Adults: 1 to 2 ampoules, intramuscularly or subcutaneously, 1-3 times daily.\
    For the management of acute stone colics: 1 or 2 ampoules by slow intravenous injection.',

    '3 pills twice a day. Only for children older than 3 y.o., do not take together with paracetamol',

    'the procure is only allowed no often that once in 3 months',

    '1 pill per day 2 hours for the meal. Not allowed for pregnant and children younger 7 years',

    'Recommended for people with suspected epilepsy.No contraindications.\
     Please do not drink alcohol 1 day before the procedure',

    'The recommended initial dose for adults is 1 mg at bedtime; however, some patients may need a \
    2 mg dose. In healthy elderly patients, 1 mg is also the appropriate starting dose, but increases\
     should be initiated with particular care. In small or debilitated older patients, \
     a starting dose of 0.5 mg, while only marginally effective in the overall elderly population, \
     should be considered.',
    'Clorazepate comes as a tablet to take by mouth. It is usually taken one to three times a day. \
    Follow the directions on your prescription label carefully, and ask your doctor or pharmacist to \
    explain any part you do not understand. Take clorazepate exactly as directed.If you are taking \
    clorazepate to treat anxiety or seizures, your doctor will probably start you on a low dose of \
    clorazepate and gradually increase your dose. If you are taking clorazepate to treat alcohol\
     withdrawal, your doctor will probably start you on a high dose of clorazepate and gradually \
     decrease your dose as your symptoms are controlled.Clorazepate can be habit-forming. Take\
      clorazepate exactly as directed. Do not take a larger dose, take it more often, or take it for a\
       longer time than prescribed by your doctor.',

    'Treatment for patients with anxiety should be initiated with a dose of 0.25 to 0.5 mg given three times daily.\
     The dose may be increased to achieve a maximum therapeutic effect, at intervals of 3 to 4 days,\
      to a maximum daily dose of 4 mg, given in divided doses. The lowest possible effective dose \
      should be employed and the need for continued treatment reassessed frequently. The risk of \
      dependence may increase with dose and duration of treatment.In all patients, dosage should be \
      reduced gradually when discontinuing therapy or when decreasing the daily dosage. Although there \
      are no systematically collected data to support a specific discontinuation schedule, it is \
      suggested that the daily dosage be decreased by no more than 0.5 mg every 3 days. Some patients \
      may require an even slower dosage reduction.',

    'Swallow the extended-release tablets whole with a full glass of water. Do not break, crush, or chew them.\
    Swallow the delayed-release tablets with a full glass of water.Chewable aspirin tablets may be chewed,\
     crushed, or swallowed whole. Drink a full glass of water, immediately after taking these tablets.Ask\
      a doctor before you give aspirin to your child or teenager. Aspirin may cause Reyes syndrome\
       (a serious condition in which fat builds up on the brain, liver, and other body organs) in children\
        and teenagers, especially if they have a virus such as chicken pox or the flu.'
]

analyze_result = ['Good', 'Bad', '4,4 mmol/L ', '10,0 mmol/L', '6,8 mmol/L',
                  'twice above the norm', 'slightly exceed the norm', 'slightly lower the norm',
                  'in critically low region']

diagnose_name = [
    'Obesity',
    'Flu',
    'Constipation',
    'Asthma (Pediatric)',
    'Headache, Migraine',
    'Substance Use Disorders',
    'Depression',
    'Hypertension',
    'Food Allergy',
    'Anxiety Disorder',
    'Speech Defects',
    'Autism Spectrum Disorder',
    'Intellectual Disability',
    'Tourette Syndrome',
    'Headache, Chronic Daily',
    'Congenital Heart Defects, all',
    'Seizure Disorder',
    'Hearing Loss',
    'Cancer',
    'AF arrhythmia',
    'Poisoning',
    'Insult',
    'Heart Attack',
    'Ischemia'
]

diagnose_treatment = ['grammidin and urine test', 'painkillers and good sleeping',
                      'regular fitness and less eating', 'blood test', 'EEG and sedative',
                      'strepsils and paracetamol', 'cardoi pills 2 and stay in bed for a week',
                      'strepsils and physiotherapy', 'consultation from neurologist',
                      'stop physical activity and analgesics', 'surgeon', 'taking less noshpa and better sleeping'
                      ]


def gen_date(min_year=2000, max_year=datetime.datetime.now().year):
    start = datetime.datetime(min_year, 1, 1, 00)
    years = max_year - min_year + 1
    end = start + datetime.timedelta(days=365 * years)
    return (start + (end - start) * random()).replace(second=0, microsecond=0)


def gen_date_later(date):
    return (date + datetime.timedelta(days=randrange(3, 1000)))


def gen_working_hours(mode):
    min = [0, 15, 30, 45]
    if mode == 1:
        time_from = datetime.time(hour=randrange(0, 8),
                                  minute=sample(min, 1)[0])
        time_to = datetime.time(hour=time_from.hour + 8,
                                minute=sample(min, 1)[0])
    elif mode == 2:
        time_from = datetime.time(hour=randrange(8, 16),
                                  minute=randrange(0, 59))
        time_to = datetime.time(hour=time_from.hour + 8,
                                minute=sample(min, 1)[0])
    else:
        time_from = datetime.time(hour=randrange(16, 24),
                                  minute=sample(min, 1)[0])
        time_to = datetime.time(hour=time_from.hour + 8 - 24,
                                minute=sample(min, 1)[0])
    return time_from.replace(second=0, microsecond=0), time_to.replace(second=0, microsecond=0)


def gen_boolean():
    return randrange(0, 2) == 1


def gen_sex_and_name():
    sex = gen_boolean()

    if sex:
        full_name = f'{choice(fem_name)} {choice(surnames)}'
    else:
        full_name = f'{choice(male_name)} {choice(surnames)}'

    return sex, full_name


def create_snn(num=num_of_patients):
    snns = set()
    while len(snns) <= num:
        snns.add(randint(100000, 1000000))
    return snns



a= gen_date().date()
print(a)
print(gen_date_later(a))
