# %%

from scrape.model.program_catalogue import ProgramCatalogue
from scrape.page.courses_in_program import get_program_page
from scrape.parse import (clean_whitespace, parse_program)

# %%

from scrape.page import fields_at_levels

all_fields = fields_at_levels.get_all_fields()
# %%

catalogue = ProgramCatalogue()

# %%

empty_study_fields = {
    study_level: tuple((
        field_name for field_name, programs in fields.items()
        if not programs
    ))
    for study_level, fields in catalogue.items()
}


# @todo: implement the above as a test case
# @todo: improve testing for parser
# @todo: improve parsing until this list is empty

#%%


# %%

def example_program_requirements():
    global level, field, program
    level = 'Undergraduate'
    field = 'Bioinformatics'
    program = 'Bachelor of Science Four-year (B.Sc. Four-year)'
    program_page = get_program_page(program, field, level)
    content = clean_whitespace(program_page)
    data = parse_program(content)
    return data


prog_reqs = example_program_requirements()
