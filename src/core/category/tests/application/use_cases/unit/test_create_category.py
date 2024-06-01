from unittest.mock import MagicMock
from uuid import UUID

import pytest

from src.core.category.application.use_cases.category_repository import CategoryRepository
from src.core.category.application.use_cases.create_category import CreateCategoryRequest, CreateCategory
from src.core.category.application.use_cases.exceptions import InvalidCategoryData


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        request = CreateCategoryRequest(
            name="Films",
            description="Films about action",
            is_active=True  # default value
        )

        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response.id, UUID)
        assert mock_repository.create.called is True

    def test_create_category_with_invalid_data(self):
        use_case = CreateCategory(
            repository=MagicMock(CategoryRepository))

        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exc_info:
            use_case.execute(CreateCategoryRequest(name=""))

        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == "name cannot be empty"
