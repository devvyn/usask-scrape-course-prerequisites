# %%
"""
fn get list of course details data:
    get list of study_levels
    get list of program_subjects_urls
    for program subject details page in program_subjects_urls:
        get list of program urls
        for program details page in program urls:
            get list of course urls
            for course details page in course urls:
                get course details data
"""

# %%
import subjects

"""
> get list of study_levels
> get list of program_subjects_urls
"""

program_subjects = subjects.fetch_subjects_by_study_level()

# %%

import urllib.parse
import programs

"""
> for program subject details page in program type urls:
>     get list of program urls
"""

# temporary bypass of loop
PROGRAM_SUBJECT_PAGE_PATH_BIOINFORMATICS = \
    '../arts-and-science/bioinformatics/index.php'  # @todo: delete this
# line ASAP
program_subject_page_path = PROGRAM_SUBJECT_PAGE_PATH_BIOINFORMATICS

# for program_subject_page_path in program_subjects:
program_subject_page_url = urllib.parse.urljoin(subjects.LIST_OF_PROGRAMS,
                                                program_subject_page_path)
programs_by_subject = programs.fetch_programs_by_subject(
    program_subject_page_url)

# %%

"""
>         for program details page in program urls:
>             get list of courses urls
"""

import courses.courses_by_course_code

# temp bypass of loop
PROGRAM_PAGE_URL_BS4Y_BINF = "https://programs.usask.ca/arts-and-science/" \
                             "bioinformatics/bsc-4-bioinformatics.php"

# for program_page_url in program_page_urls:
program_page_url = PROGRAM_PAGE_URL_BS4Y_BINF
courses_by_section = courses.courses_by_course_code.fetch_courses_by_section(
    program_page_url)
