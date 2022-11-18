ES_FIELDS = {
    'index': {
        'Poetry_Foundation' : 'poetry-foundation',
        'News_Articles': 'all-the-news',
        'SEC_Texts': 'sec_texts',
        'China_news' : 'china_newstranscripts',
        'Care_Reviews':'care_reviews',
        'caselaw_env':'caselaw_env',
        'Covid':'covid_v4',
        'Pubmed': 'pubmed_v3',
        'PMC': 'pmc_test',
        'JSTOR': 'jstor',
        'foster': 'foster_care_note',
        'foster_encounter': 'foster_care_encounter',
        'Archaeology': 'archaeology',
        'Latin': 'latin',
        'Ehealth': 'alzheimer_threads',
        'TCP': 'tcp',
        'ACJ': 'ac_justice',
        'AA': 'anesthesiology',
        'CaseLaw_v2': 'case_law_v2',
        'CCHMC' : 'cchmc_notes',
        'TED' : 'ted_talks',
        'Pulmonary' : 'pulmonary_notes',
        'Ehealth_Threads': 'alzheimer_threads', 
        'Cannabis_News':'cannabis',
        'NPO_taxforms':'npo_990forms',
        'OHNPO_taxforms': 'ohio_npo_essential',
        'Pubmed_COI': 'coi_statements',
        'Reddit' : 'parenting_subreddit', 
        'SAA_Abstracts': 'arch_abstracts',
        'Med_Applications': 'family_medicine',
        'Mayerson' : 'mayerson',
        'Mayerson_qna' : 'mayerson_qna',
        'hathitrust_novels' : 'hathitrust_novels',
        'early_modern':'early_modern', 
        'NYNPO_taxforms': 'nynpo_taxforms',
        'Hathi_Climate' : 'hathi_climate',
        'Hathi_Rand' : 'hathi_climate_rand',
        'NYT_China' : 'nyt-china',
        'WSJ_China' : 'wsj_china',
        'WAPO_China': 'wapo_china',
        'US_Poetics' : 'us_poetics',
        'space_news': 'space_news',
        'chicago-novels' : 'chicago-novels', 
        'space_tvnews' : 'space_tvnews'

    },
    'id': {
        'Poetry_Foundation' : 'pmid',
        'News_Articles': 'id',
        'SEC_Texts': 'id',
        'China_news' : 'id',
        'Care_Reviews':'UUID',
        'caselaw_env':'id',
        'Covid':'paper_id',
        'Pubmed': 'PMID',
        'PMC': 'PMCID',
        'JSTOR': 'JSTOR_ID',
        'foster': 'NOTE_ID',
        'foster_encounter': 'NOTE_ID',
        'CaseLaw': 'CaseID',
        'Archaeology': 'ArticleID',
        'Latin': 'ArticleID',
        'Ehealth': 'id',
        'TCP': 'TCPID',
        'ACJ': 'Pid',
        'AA': 'SID',
        'CaseLaw_v2': 'CaseID',
        'CCHMC' : 'NoteID',
        'TED' : 'Talk_ID',
        'Pulmonary': 'NoteID',
        'Ehealth_Threads': 'id',
        'Cannabis_News':'id', 
        'NPO_taxforms':'id',
        'OHNPO_taxforms':'id',
        'Pubmed_COI': 'pmid',
        'Reddit' : 'ID',
        'SAA_Abstracts': 'id', 
        'Med_Applications': 'id',
        'Mayerson' : 'case_num',
        'Mayerson_qna' : 'case_no',
        'hathitrust_novels' : 'id',
        'early_modern' : 'id', 
        'NYNPO_taxforms': 'ein',
        'Hathi_Climate' : 'hathi_id',
        'Hathi_Rand' : 'hathi_id',
        'NYT_China' : 'uid',
        'WSJ_China' : 'uid',
        'WAPO_China' : 'uid',
        'US_Poetics' : 'uid',
        'space_news' : 'id',
        'chicago-novels' : 'id',
        'space_tvnews' : 'id'
    },
    'abstract': {
        'Poetry_Foundation' : 'text',
        'News_Articles': 'title',
        'SEC_Texts': 'title',
        'China_news' : 'description',
        'Care_Reviews':'reviewText',
        'caselaw_env':'title',
        'Covid':'abstract',
        'Pubmed': 'AbstractText',
        'PMC': 'Abstract',
        'JSTOR': 'FullText',
        'CaseLaw': 'FullText',
        'Archaeology': 'FullText',
        'Latin': 'FullText',
        'Ehealth': 'text',
        'TCP': 'FullText',
        'ACJ': 'FullText',
        'AA': 'Abstract',
        'CaseLaw_v2': 'FullText',
        'CCHMC' : 'FullText',
        'TED' : 'FullText',
        'Pulmonary': 'FullText',
        'Ehealth_Threads': 'text', 
        'Cannabis_News':'text', 
        'NPO_taxforms':'text',
        'OHNPO_taxforms': 'text', 
        'Pubmed_COI': 'coi',
        'Reddit' : 'FullText',
        'SAA_Abstracts': 'text',
        'Med_Applications': 'text',
        'Mayerson' : 'text',
        'Mayerson_qna' : 'text',
        'hathitrust_novels' : 'page_tokens',
        'early_modern' : 'text', 
        'NYNPO_taxforms': 'text',
        'Hathi_Climate' : 'text',
        'Hathi_Rand' : 'text',
        'NYT_China' : 'text',
        'WSJ_China' : 'text',
        'WAPO_China' : 'text',
        'US_Poetics' : 'url',
        'space_news' : 'text',
        'chicago-novels' : 'genre',
        'space_tvnews' : 'abstract'
    },
    'full_text': {
        'Poetry_Foundation' : 'text',
        'News_Articles': 'article',
        'SEC_Texts': 'text',
        'China_news' : 'text',
        'Care_Reviews':'reviewText',
        'caselaw_env':'text',
        'Covid':'fullText',
        'Pubmed': 'AbstractText',
        'PMC': 'FullText',
        'JSTOR': 'FullText',
        'foster': 'HPI_SOCIAL_HISTORY',
        'foster_encounter': 'HPI_SOCIAL_HISTORY',
        'CaseLaw': 'FullText',
        'Archaeology': 'FullText',
        'Latin': 'FullText',
        'Ehealth': 'text',
        'TCP': 'FullText',
        'ACJ': 'FullText',
        'AA': 'Abstract',
        'CaseLaw_v2': 'FullText',
        'CCHMC' : 'FullText',
        'TED' : 'FullText',
        'Pulmonary': 'FullText',
        'Ehealth_Threads': 'text',
        'Cannabis_News':'text', 
        'NPO_taxforms':'text',
        'OHNPO_taxforms':'text',
        'Pubmed_COI': 'coi',
        'Reddit' : 'FullText',
        'SAA_Abstracts': 'text', 
        'Med_Applications': 'text',
        'Mayerson' : 'text',
        'Mayerson_qna' : 'text',
        'hathitrust_novels' : 'page_tokens',
        'early_modern' : 'text', 
        'NYNPO_taxforms': 'text',
        'Hathi_Climate' : 'text',
        'Hathi_Rand' : 'text',
        'NYT_China' : 'text',
        'WSJ_China' : 'text',
        'WAPO_China' : 'text',
        'US_Poetics' : 'text',
        'space_news' : 'text',
        'chicago-novels' : 'text',
        'space_tvnews' : 'text'
    },
    'doc_title' :
        {
        'Poetry_Foundation' : 'title',
        'News_Articles': 'title',
        'SEC_Texts': 'title',
        'china_newstranscripts' : 'title',
        'China_news' : 'title',
        'Care_Reviews':'doc_title',
        'caselaw_env':'title',
        'Covid': 'title',
        'Pubmed': 'ArticleTitle',
        'PMC': 'ArticleTitle',
        'JSTOR': 'ArticleTitle',
        'foster': 'PAT_ID',
        'foster_encounter': 'PAT_ID',
        'CaseLaw': 'Name',
        'Archaeology': 'ArticleTitle',
        'Latin': 'ArticleTitle',
        'Ehealth': 'TopicID',
        'TCP': 'ArticleTitle',
        'ACJ': 'ArticleTitle',
        'AA': 'ArticleTitle',
        'CaseLaw_v2': 'Name',
        'CCHMC' : 'NoteID',
        'TED' : 'Name',
        'Pulmonary': 'NoteID',
        'Ehealth_Threads': 'entry_id', 
        'Cannabis_News': 'link', 
        'Pubmed_COI': 'article',
        'Reddit' : 'ID',
        'NPO_taxforms': 'id',
        'OHNPO_taxforms': 'id',
        'SAA_Abstracts': 'id', 
        'Med_Applications': 'title',
        'Mayerson' : 'case_num',
        'Mayerson_qna' : 'case_no',
        'hathitrust_novels' : 'title',
        'early_modern' : 'title', 
        'NYNPO_taxforms': 'title',
        'Hathi_Climate' : 'title',
        'Hathi_Rand' : 'title',
        'NYT_China' : 'title',
        'WSJ_China' : 'title',
        'WAPO_China' : 'title',
        'US_Poetics' : 'title',
        'space_news' : 'title',
        'chicago-novels' : 'title',
        'space_tvnews' : 'title'
        },
    'author' :
        {
        'Poetry_Foundation' : 'author',
        'News_Articles': 'author',
        'SEC_Texts': 'title',
        'China_news' : 'program',
        'Care_Reviews':'dataSource',
        'caselaw_env':'URL',
        'Covid': 'authors',
        'PMC': 'ArticleTitle',
        'JSTOR': 'Authors',
        'TCP': 'Authors',
        'AA': 'Authors',
        'TED' : 'Speaker_1',
        'Pubmed_COI': 'authors',
        'Reddit' : 'ID',
        'Cannabis_News': 'title', 
        'Mayerson' : 'interviewer',
        'Mayerson_qna' : 'interviewer',
        'hathitrust_novels' : 'author',
        'early_modern' : 'author', 
        'NYNPO_taxforms': 'title',
        'Hathi_Climate' : 'author',
        'Hathi_Rand' : 'author',
        'NYT_China' : 'author',
        'WSJ_China' : 'author',
        'WAPO_China' : 'author',
        'US_Poetics' : 'author',
        'space_news' : 'author',
        'chicago-novels' : 'author',
        'space_tvnews' : 'title'
        },
    'date': {
        'Poetry_Foundation' : 'date',
        'News_Articles': 'date',
        'SEC_Texts': 'date',
        'China_news' : 'date',
        'Care_Reviews':'reviewDate',
        'caselaw_env':'date',
        'Covid':'date',
        'Pubmed': 'ReleaseDate',
        'PMC': 'ReleaseDate',
        'JSTOR': 'ReleaseDate',
        'foster': 'TODO',
        'CaseLaw': 'DecisionDate',
        'Archaeology': 'ReleaseDate',
        'Latin': 'No_date',
        'Ehealth': 'date',
        'TCP': 'PubDate',
        'ACJ': 'PubDate',
        'AA': 'Date',
        'CaseLaw_v2': 'DecisionDate',
        'CCHMC' : 'NoteDate',
        'TED' : 'PubDate',
        'Pulmonary': 'NoteDate',
        'Ehealth_Threads': 'date', 
        'Cannabis_News':'date', 
        'NPO_taxforms':'date',
        'OHNPO_taxforms': 'date',
        'Cannabis_News':'date',
        'Pubmed_COI': 'pub_year',
        'Reddit' : 'Date',
        'SAA_Abstracts': 'date', 
        'Med_Applications': 'date',
        'Mayerson' : 'file_date',
        'Mayerson_qna' : 'file_date',
        'hathitrust_novels' : 'date',
        'early_modern' : 'date', 
        'NYNPO_taxforms': 'date',
        'Hathi_Climate' : 'date',
        'Hathi_Rand' : 'date',
        'NYT_China' : 'date',
        'WSJ_China' : 'date',
        'WAPO_China' : 'date',
        'US_Poetics' : 'date',
        'space_news' : 'date',
        'chicago-novels' : 'date',
        'space_tvnews' : 'date'
    },
    'doc_type': {
        'foster': 'note',
        'foster_encounter': 'note'
    },
    'info': {
        'Poetry_Foundation' : ['title', 'author'],
        'News_Articles': ['title', 'url', 'publication', 'section'],
        'SEC_Texts': ['title', 'date'],
        'china_newstranscripts' : ['title', 'date', 'program'],
        'China_news' : ['title', 'date', 'program'],
        'Care_Reviews':['businessTitle','dataSource','directURL'],
        'caselaw_env':['case_ID','title', 'date'],
        'Covid':['paper_id','bib_entries','authors'],
        'Pubmed': ['PMID', 'ReleaseDate'],
        'PMC': ['ID', 'Journal', 'Pub Date', 'Authors'],
        'JSTOR': ['ID', 'Journal', 'Pub Date', 'Authors'],
        'foster': ['TODO'],
        'CaseLaw': ['ID', 'Date'],
        'Ehealth': ['id', 'date'],
        'TCP': ['ID', 'PubDate', 'Authors'],
        'ACJ': ['ID', 'PubDate'],
        'CaseLaw_v2': ['ID', 'Date'],
        'CCHMC' : ['NoteID','NoteDate'],
        'TED' : ['Talk_ID', 'PubDate'],
        'Pulmonary':['NoteID', 'NoteDate'],
        'Ehealth_Threads': ['id', 'date'], 
        'Cannabis_News':['id', 'date'],
        'NPO_taxforms':['id', 'date'],
        'OHNPO_taxforms':['id', 'date'],
        'Cannabis_News':['id', 'date'], 
        'Pubmed_COI': ['pmid','journal', 'authors'],
        'Reddit' : ['ID', 'Date'],
        'SAA_Abstracts': ['id', 'date'], 
        'Med_Applications': ['id', 'date'],
        'Mayerson' : ['case_num', 'file_date'],
        'Mayerson_qna' : ['case_no', 'file_date'],
        'hathitrust_novels' : ['title', 'date'],
        'early_modern' : ['title', 'date'],
        'NYNPO_taxforms': ['title', 'date'],
        'Hathi_Climate' : ['title', 'page'],
        'Hathi_Rand' : ['title', 'page'],
        'NYT_China' : ['title', 'author'],
        'WSJ_China' : ['title', 'author'],
        'WAPO_China' : ['title', 'author'],
        'US_Poetics' : ['title', 'author'],
        'space_news' : ['title', 'author'],
        'chicago-novels' : ['title', 'author'],
        'space_tvnews' : ['title', 'abstract'],
     }
}
MAX_NUM_DOC_VIS = {
    'Poetry_Foundation' : 16000,
    'News_Articles': 22000,
    'SEC_Texts': 22000,
    'china_newstranscripts' : 189000,
    'China_news' : 189000,
    'Care_Reviews': 40000,
    'caselaw_env':121000,
    'Covid': 144000,
    'Pubmed': 20000,
    'PMC': 20000,
    'JSTOR': 4000,
    'foster': 10000,
    'CaseLaw': 6000,
    'Archaeology': 5000,
    'Latin': 20000,
    'Ehealth': 20000,
    'TCP': 1500,
    'ACJ': 20000,
    'searchpage' : 144000,
    'CaseLaw_v2' : 326000,
    'AA' : 23000,
    'CCHMC' : 20000,
    'TED' : 20000,
    'Pulmonary': 20000,
    'Ehealth_Threads': 20000,
    'Cannabis_News': 15000, 
    'NPO_taxforms': 20000,
    'OHNPO_taxforms': 10000,
    'Cannabis_News': 14000,
    'Pubmed_COI': 20000,
    'Reddit' : 50000,
    'SAA_Abstracts': 20000, 
    'Med_Applications': 4000,
    'Mayerson' : 20000,
    'Mayerson_qna' : 20000,
    'hathitrust_novels' : 2000,
    'early_modern' : 6000, 
    'NYNPO_taxforms': 45000,
    'Hathi_Climate' : 5000,
    'Hathi_Rand' : 5000,
    'NYT_China' : 80000,
    'WSJ_China' : 31000,
    'WAPO_China': 10000,
    'US_Poetics' : 52000,
    'space_news' : 10000,
    'chicago-novels' : 18000000,
    'space_tvnews' : 15000
}


# 'index': {
#     'Poetry_Foundation' : 'poetry-foundation',
#     'News_Articles': 'all-the-news',
#     'SEC_Texts': 'sec_texts',
#     'China_news' : 'china_newstranscripts',
#     'Care_Reviews':'care_reviews',
#     'caselaw_env':'caselaw_env',
#     'Covid':'covid_v4',
#     'Pubmed': 'pubmed_v3',
#     'PMC': 'pmc_test',
#     'JSTOR': 'jstor',
#     'foster': 'foster_care_note',
#     'foster_encounter': 'foster_care_encounter',
#     'Archaeology': 'archaeology',
#     'Latin': 'latin',
#     'Ehealth': 'alzheimer_threads',
#     'TCP': 'tcp',
#     'ACJ': 'ac_justice',
#     'AA': 'anesthesiology',
#     'CaseLaw_v2': 'case_law_v2',
#     'CCHMC' : 'cchmc_notes',
#     'TED' : 'ted_talks',
#     'Pulmonary' : 'pulmonary_notes',
#     'Ehealth_Threads': 'alzheimer_threads', 
#     'Cannabis_News':'cannabis',
#     'NPO_taxforms':'npo_990forms',
#     'OHNPO_taxforms': 'ohio_npo_essential',
#     'Pubmed_COI': 'coi_statements',
#     'Reddit' : 'parenting_subreddit', 
#     'SAA_Abstracts': 'arch_abstracts',
#     'Med_Applications': 'family_medicine',
#     'Mayerson' : 'mayerson',
#     'Mayerson_qna' : 'mayerson_qna',
#     'hathitrust_novels' : 'hathitrust_novels',
#     'early_modern':'early_modern', 
#     'NYNPO_taxforms': 'nynpo_taxforms',
#     'Hathi_Climate' : 'hathi_climate',
#     'Hathi_Rand' : 'hathi_climate_rand',
#     'NYT_China' : 'nyt-china',
#     'WSJ_China' : 'wsj_china',
#     'WAPO_China': 'wapo_china',
#     'US_Poetics' : 'us_poetics',
#     'space_news': 'space_news'
# },


datasetNames = {
	'archaeology': {
            'num_docs': 50000,
         'description': 'Archaeology journal Articles',
         's3_names': {
            'bert': '_Archaeology_umap_kmeans'},
            'display_name' : 'Archaeology',
         'database': 'Archaeology'},
	'anesthesiology': {
            'num_docs': 50000,
         'description': 'Anesthesiology publication abstracts',
         's3_names': {
            'bert': '_AA_umap_kmeans'},
            'display_name' : 'Anesthesiology Abstracts',
         'database': 'AA'},

    'case_law_v2' : {
            'num_docs': 50000,
         'description': 'Caselaw antitrust results',
         's3_names': {
            'bert': 'antitrust_CaseLaw_v2_umap_kmeans'},
            'display_name' : 'Caselaw Antitrust',
         'database': 'CaseLaw_v2'},

	'chinanews': {
            'num_docs': 50000,
         'description': 'news transcripts mentioning china',
         's3_names': {
            'bert': '_China_news_umap_kmeans'},
            'display_name' : 'China News Transcripts',
         'database': 'China_news'},
     'carereviews': {
            'num_docs': 30000,
         'description': 'This is a sample description for a dataset.',
         's3_names': {
            'bert': '_Care_Reviews_umap_kmeans'},
            'display_name' : 'Urgent Care Reviews',
         'database': 'Care_Reviews'},
     'covid': {
            'num_docs': 144000,
         'description': 'Covid CDC dataset as of November 2020.',
         's3_names': {
            'bert': '_Covid_umap_kmeans',},
            'display_name' : 'CDC Covid Dataset',
         'database': 'Covid'},
     'pubmed': {
            'num_docs': 2000000,
         'description': 'Pubmed abstracts mentioning climate.',
         's3_names': {
            'bert': 'climate_Pubmed_umap_kmeans'},
            'display_name' : 'Pubmed Abstracts climate',
         'database': 'Pubmed'},
     'tcp': {
            'num_docs': 1500,
         'description': 'Old english works',
         's3_names': {
            'bert': '_TCP_umap_kmeans'},
            'display_name' : 'Text Creation Partnership',
            'database': 'TCP'},

       'reddit': {
            'num_docs': 45000,
         'description': 'Comments pulled from the /r/Parenting subreddit.',
         's3_names': {
            'bert': '_Reddit_umap_kmeans',},
            'display_name' : '/r/Parenting',
         'database': 'Reddit'},
     'medapplications': {
        'num_docs': 4000,
         'description': '',
         's3_names': {
            'bert': 'Med_Applications_umap_kmeans',
			},
			'display_name' : 'Medical School Applications',
         'database': 'Med_Applications'},
      'nyt-china' : {
      		'num_docs' : 45000,
      		'description' : 'New York Times articles mentioning China',
      		's3_names': {
            'bert': '_NYT_China_umap_kmeans'
            	},
            	'display_name' : 'NYTimes China',
         'database': 'NYT_China'
         },
       # 'pulmonary_notes' :{
      	# 	'num_docs' : 45000,
      	# 	'description' : 'Pulmonary notes',
      	# 	's3_names': {
       #      'bert': '_Pulmonary_umap_kmeans'
       #      	},
       #   'database': 'Pulmonary'
       #   },
     'poetryfoundation': {
         'num_docs': 15692,
         'description': 'Open source collection of poems from the Poetry Foundation',
         's3_names': {
            'bert': '_Poetry_foundation_umap_kmeans',
      		},
      		'display_name' : 'Poetry Foundation',
         'database': 'Poetry_Foundation'},
   	 'wapo_china': {
   	 	'num_docs': 15692,
         'description': 'Washington post articles mentioning China',
         's3_names': {
            'bert': '_WAPO_China_umap_kmeans',},
            'display_name' : 'Washington Post China',
         'database': 'WAPO_China'},
      'wsj_china': {
   	 	'num_docs': 15692,
         'description': 'Wall St. Journal articles mentioning China',
         's3_names': {
            'bert': '_WSJ_China_umap_kmeans',},
            'display_name' : 'WSJ China',
         'database': 'WSJ_China'}

}


