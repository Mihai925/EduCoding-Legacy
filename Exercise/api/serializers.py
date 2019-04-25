from Exercise.models import Exercise, ExerciseTests
from rest_framework import serializers

class ExerciseTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseTests
        fields = ('input', 'expected_output')


class ExerciseSerializer(serializers.ModelSerializer):
    tests = ExerciseTestsSerializer(many=True)

    class Meta:
        model = Exercise
        fields = ('ex_id', 'title', 'description', 'content', 'has_tests', 'tests', 'language')
        depth = 1

    def create(self, validated_data):
        tests = validated_data.pop('tests')
        exercise = super(ExerciseSerializer, self).create(validated_data)

        # TODO make it safer
        user = self.context['request'].user
        exercise.author = user

        for test in exercise.tests.all():
            test.delete()

        for test in tests:
            exercise_test = ExerciseTests.objects.create(**test)
            exercise.tests.add(exercise_test)

        exercise.save()
        return exercise

    def update(self, instance, validated_data):
        tests = validated_data.pop('tests')

        exercise = super(ExerciseSerializer, self).update(instance, validated_data)


        for test in exercise.tests.all():
            test.delete()

        for test in tests:
            exercise_test = ExerciseTests.objects.create(**test)
            exercise.tests.add(exercise_test)
        return exercise



