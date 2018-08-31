from django.test.client import RequestFactory
    get_diff_data_chunks_info,
    get_original_file,
class GetDiffDataChunksInfoTests(TestCase):
    """Unit tests for get_diff_data_chunks_info."""

    def test_with_basic_diff(self):
        """Testing get_diff_data_chunks_info with a basic one-chunk diff"""
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -10,7 +12,10 @@\n'
                b' #\n'
                b' #\n'
                b' #\n'
                b'-# old line\n'
                b'+# new line\n'
                b'+# new line\n'
                b'+# new line\n'
                b'+# new line\n'
                b' #\n'
                b' #\n'
                b' #\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 9,
                        'chunk_len': 7,
                        'changes_start': 12,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 11,
                        'chunk_len': 10,
                        'changes_start': 14,
                        'changes_len': 4,
                    },
                },
            ])

    def test_with_multiple_chunks(self):
        """Testing get_diff_data_chunks_info with multiple chunks in a diff"""
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -10,7 +12,10 @@\n'
                b' #\n'
                b' #\n'
                b' #\n'
                b'-# old line\n'
                b'+# new line\n'
                b'+# new line\n'
                b'+# new line\n'
                b'+# new line\n'
                b' #\n'
                b' #\n'
                b' #\n'
                b'@@ -23,7 +40,7 @@\n'
                b' #\n'
                b' #\n'
                b' #\n'
                b'-# old line\n'
                b'+# new line\n'
                b' #\n'
                b' #\n'
                b' #\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 9,
                        'chunk_len': 7,
                        'changes_start': 12,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 11,
                        'chunk_len': 10,
                        'changes_start': 14,
                        'changes_len': 4,
                    },
                },
                {
                    'orig': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 22,
                        'chunk_len': 7,
                        'changes_start': 25,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 39,
                        'chunk_len': 7,
                        'changes_start': 42,
                        'changes_len': 1,
                    },
                },
            ])

    def test_with_multiple_chunks_no_context(self):
        """Testing get_diff_data_chunks_info with multiple chunks and no
        context
        """
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -13,1 +15,4 @@\n'
                b'-# old line\n'
                b'+# new line\n'
                b'+# new line\n'
                b'+# new line\n'
                b'+# new line\n'
                b'@@ -26,1 +43,1 @@\n'
                b'-# old line\n'
                b'+# new line\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 0,
                        'chunk_start': 12,
                        'chunk_len': 1,
                        'changes_start': 12,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 0,
                        'chunk_start': 14,
                        'chunk_len': 4,
                        'changes_start': 14,
                        'changes_len': 4,
                    },
                },
                {
                    'orig': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 0,
                        'chunk_start': 25,
                        'chunk_len': 1,
                        'changes_start': 25,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 0,
                        'chunk_start': 42,
                        'chunk_len': 1,
                        'changes_start': 42,
                        'changes_len': 1,
                    },
                },
            ])

    def test_with_all_inserts(self):
        """Testing get_diff_data_chunks_info with all inserts"""
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -10,6 +12,10 @@\n'
                b' #\n'
                b' #\n'
                b' #\n'
                b'+# new line\n'
                b'+# new line\n'
                b'+# new line\n'
                b'+# new line\n'
                b' #\n'
                b' #\n'
                b' #\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 6,
                        'post_lines_of_context': 0,
                        'chunk_start': 9,
                        'chunk_len': 6,
                        'changes_start': 9,
                        'changes_len': 0,
                    },
                    'modified': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 11,
                        'chunk_len': 10,
                        'changes_start': 14,
                        'changes_len': 4,
                    },
                },
            ])

    def test_with_all_deletes(self):
        """Testing get_diff_data_chunks_info with all deletes"""
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -10,10 +12,6 @@\n'
                b' #\n'
                b' #\n'
                b' #\n'
                b'-# old line\n'
                b'-# old line\n'
                b'-# old line\n'
                b'-# old line\n'
                b' #\n'
                b' #\n'
                b' #\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 9,
                        'chunk_len': 10,
                        'changes_start': 12,
                        'changes_len': 4,
                    },
                    'modified': {
                        'pre_lines_of_context': 6,
                        'post_lines_of_context': 0,
                        'chunk_start': 11,
                        'chunk_len': 6,
                        'changes_start': 11,
                        'changes_len': 0,
                    },
                },
            ])

    def test_with_complex_chunk(self):
        """Testing get_diff_data_chunks_info with complex chunk containing
        inserts, deletes, and equals
        """
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -10,9 +12,12 @@\n'
                b' #\n'
                b' #\n'
                b' #\n'
                b'+# new line\n'
                b' #\n'
                b'-# old line\n'
                b'+# new line\n'
                b'+# new line\n'
                b' #\n'
                b'+# new line\n'
                b' #\n'
                b' #\n'
                b' #\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 4,
                        'post_lines_of_context': 4,
                        'chunk_start': 9,
                        'chunk_len': 9,
                        'changes_start': 13,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 11,
                        'chunk_len': 12,
                        'changes_start': 14,
                        'changes_len': 6,
                    },
                },
            ])

    def test_with_change_on_first_line(self):
        """Testing get_diff_data_chunks_info with change on first line"""
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -1,4 +1,5 @@\n'
                b'-# old line\n'
                b'+# new line\n'
                b'+# new line\n'
                b' #\n'
                b' #\n'
                b' #\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 3,
                        'chunk_start': 0,
                        'chunk_len': 4,
                        'changes_start': 0,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 3,
                        'chunk_start': 0,
                        'chunk_len': 5,
                        'changes_start': 0,
                        'changes_len': 2,
                    },
                },
            ])

    def test_with_change_on_second_line(self):
        """Testing get_diff_data_chunks_info with change on second line"""
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -1,5 +1,6 @@\n'
                b' #\n'
                b'-# old line\n'
                b'+# new line\n'
                b'+# new line\n'
                b' #\n'
                b' #\n'
                b' #\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 1,
                        'post_lines_of_context': 3,
                        'chunk_start': 0,
                        'chunk_len': 5,
                        'changes_start': 1,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 1,
                        'post_lines_of_context': 3,
                        'chunk_start': 0,
                        'chunk_len': 6,
                        'changes_start': 1,
                        'changes_len': 2,
                    },
                },
            ])

    def test_with_change_on_third_line(self):
        """Testing get_diff_data_chunks_info with change on third line"""
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -1,6 +1,7 @@\n'
                b' #\n'
                b' #\n'
                b'-# old line\n'
                b'+# new line\n'
                b'+# new line\n'
                b' #\n'
                b' #\n'
                b' #\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 2,
                        'post_lines_of_context': 3,
                        'chunk_start': 0,
                        'chunk_len': 6,
                        'changes_start': 2,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 2,
                        'post_lines_of_context': 3,
                        'chunk_start': 0,
                        'chunk_len': 7,
                        'changes_start': 2,
                        'changes_len': 2,
                    },
                },
            ])

    def test_with_no_lengths(self):
        """Testing get_diff_data_chunks_info with no lengths specified"""
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -1 +1 @@\n'
                b'-# old line\n'
                b'+# new line\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 0,
                        'chunk_start': 0,
                        'chunk_len': 1,
                        'changes_start': 0,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 0,
                        'chunk_start': 0,
                        'chunk_len': 1,
                        'changes_start': 0,
                        'changes_len': 1,
                    },
                },
            ])

    def test_with_header_context(self):
        """Testing get_diff_data_chunks_info with class/functino context
        shown in the header
        """
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -10,7 +12,10 @@ def foo(self):\n'
                b' #\n'
                b' #\n'
                b' #\n'
                b'-# old line\n'
                b'+# new line\n'
                b'+# new line\n'
                b'+# new line\n'
                b'+# new line\n'
                b' #\n'
                b' #\n'
                b' #\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 9,
                        'chunk_len': 7,
                        'changes_start': 12,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 3,
                        'post_lines_of_context': 3,
                        'chunk_start': 11,
                        'chunk_len': 10,
                        'changes_start': 14,
                        'changes_len': 4,
                    },
                },
            ])




class GetOriginalFileTests(TestCase):
    """Unit tests for get_original_file."""

    fixtures = ['test_scmtools']

    def test_empty_parent_diff(self):
        """Testing get_original_file with an empty parent diff"""
        parent_diff = (
            b'diff --git a/empty b/empty\n'
            b'new file mode 100644\n'
            b'index 0000000..e69de29\n'
            b'\n'
        )

        diff = (
            b'diff --git a/empty b/empty\n'
            b'index e69de29..0e4b0c7 100644\n'
            b'--- a/empty\n'
            b'+++ a/empty\n'
            b'@@ -0,0 +1 @@\n'
            b'+abc123\n'
        )

        repository = self.create_repository(tool_name='Git')
        diffset = self.create_diffset(repository=repository)
        filediff = FileDiff.objects.create(
            diffset=diffset,
            source_file='empty',
            source_revision=PRE_CREATION,
            dest_file='empty',
            dest_detail='0e4b0c7')
        filediff.parent_diff = parent_diff
        filediff.diff = diff
        filediff.save()

        request_factory = RequestFactory()

        # 1 query for fetching the ``FileDiff.parent_diff_hash`` and 1 for
        # saving the object.
        with self.assertNumQueries(2):
            orig = get_original_file(
                filediff=filediff,
                request=request_factory.get('/'),
                encoding_list=['ascii'])

        self.assertEqual(orig, b'')

        # Refresh the object from the database with the parent diff attached
        # and then verify that re-calculating the original file does not cause
        # additional queries.
        filediff = (
            FileDiff.objects
            .filter(pk=filediff.pk)
            .select_related('parent_diff_hash')
            .first()
        )

        with self.assertNumQueries(0):
            orig = get_original_file(
                filediff=filediff,
                request=request_factory.get('/'),
                encoding_list=['ascii'])