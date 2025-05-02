package by.andros.android_front.auth.domain

class LoginUseCase (private val repository: AuthRepository) {
    suspend operator fun invoke(email: String, password: String): Result<Unit> {
        return repository.login(email, password)
    }
}