from pytest_bdd import scenario, given, then

from subjects import fetch_subjects_by_study_level


@scenario('../features/program_subjects_list.feature', 'get subject list',
          example_converters={
              'study_level': str,
              'subject_count': int,
              'subject': str,
          })
def test_program_subjects_list():
    pass


@given("the UofS program subject list for <study_level>")
def subjects(study_level) -> dict:
    subjects_dict = fetch_subjects_by_study_level()
    return subjects_dict[study_level]


@then("there are at least <subject_count> subjects")
def subject_count_min(subject_count, subjects):
    assert isinstance(subject_count, int)
    assert len(subjects) >= subject_count


@then("<subject> is a <study_level> subject")
def subject_is_in_study_level(subject: str, study_level: str,
                              subjects, ):
    assert subject in subjects
